# Classroom Instruction Analysis with Gemini Vision API

This Python script uploads a classroom instruction video to Google Gemini Vision API, analyzes the teacher’s instructional methods, and provides expert feedback. The feedback is printed to the console and saved in a timestamped file.

## Installation

1️⃣ Clone the Repository

```
git clone https://github.com/abhishekpillai/ai-teacher-coach.git
cd ai-teacher-coach
```

2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed, then run:

```
pip install -r requirements.txt
```

3️⃣ Set Up API Key
Get a Google Gemini API Key from Google AI Studio.
Create a .env file in the project directory and add:

```
GEMINI_API_KEY=your_google_ai_api_key
```

## Usage

### Run the Script

```
python analyze_classroom.py path/to/video.mp4
```

Replace path/to/video.mp4 with the actual video file you want to analyze.

### Example Output

```
Uploading video: classroom_video.mp4
Upload completed: gemini://video/12345abcdef
Processing video...
Video is ready: gemini://video/12345abcdef

Requesting instructional feedback...

--- Instructional Feedback ---
[Expert feedback on classroom instruction]

✅ Feedback saved to: feedback_reports/classroom_feedback_2025-01-31_14-45-10.txt
```

### Output Files

Feedback is saved in the feedback_reports/ directory in a timestamped file:

```
feedback_reports/classroom_feedback_YYYY-MM-DD_HH-MM-SS.txt
```

### Troubleshooting

- Missing API Key?

  - Ensure .env contains API_KEY=your_google_ai_api_key.

- Incorrect video path?

  - Provide the full path to the video file.

- Error uploading video?
  - Verify the file format is supported (.mp4, .mov, .avi, .webm, etc.).
