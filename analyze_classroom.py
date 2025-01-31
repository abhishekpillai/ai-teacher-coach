import os
import time
import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("API Key is missing. Set API_KEY in .env file.")

genai.configure(api_key=API_KEY)

def upload_video(video_path):
    """Uploads the video file to Gemini Vision API."""
    print(f"Uploading video: {video_path}")
    video_file = genai.upload_file(path=video_path)
    print(f"Upload completed: {video_file.uri}")

    # Wait for processing to complete
    while video_file.state.name == "PROCESSING":
        print("Processing video...", end="\r")
        time.sleep(10)
        video_file = genai.get_file(video_file.name)

    if video_file.state.name == "FAILED":
        raise ValueError("Video processing failed.")

    print(f"Video is ready: {video_file.uri}")
    return video_file

def analyze_classroom_instruction(video_file):
    """Requests feedback on classroom instruction."""
    prompt = (
        "Analyze this classroom instruction video and provide expert feedback. "
        "Assess the teacher's classroom management, student engagement, lesson clarity, "
        "and pacing. Provide constructive suggestions for improvement."
    )

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    print("\nRequesting instructional feedback...\n")
    response = model.generate_content([video_file, prompt], request_options={"timeout": 600})
    
    feedback_text = response.text

    # Print the feedback
    print("\n--- Instructional Feedback ---\n")
    print(feedback_text)

    # Save feedback to a file
    save_feedback_to_file(feedback_text)

def save_feedback_to_file(feedback_text):
    """Saves the feedback into a timestamped file."""
    os.makedirs("feedback_reports", exist_ok=True)  # Ensure the directory exists
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"feedback_reports/classroom_feedback_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Classroom Instruction Feedback\n")
        f.write("=" * 50 + "\n")
        f.write(feedback_text)
    
    print(f"\n✅ Feedback saved to: {filename}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze a classroom instruction video using Gemini Vision API.")
    parser.add_argument("video_path", help="Path to the classroom instruction video file")
    
    args = parser.parse_args()
    video_file = upload_video(args.video_path)
    analyze_classroom_instruction(video_file)
