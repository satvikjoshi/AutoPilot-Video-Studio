 # 🚀 AutoPilot Video Studio

AutoPilot Video Studio is an AI-powered video editing tool that automates the editing process while learning from user preferences.

## 🎯 Features
✔ AI-Powered Video Analysis  
✔ Smart Auto-Cuts & Scene Detection  
✔ AI Voice Cloning & TTS (Future Feature)  
✔ Self-Hosting & Standalone App  
✔ Drag & Drop File Upload  
✔ Auto-Generated Video Summaries  

## 📌 Installation Guide
1. **Clone the repository**  
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/AutoPilot-Video-Studio.git
   cd AutoPilot-Video-Studio

2. Install dependencies
    pip install -r requirements.txt

3. Run the application
    python main.py

📁 File Structure
AutoPilot-Video-Studio/
├── core/
│   ├── analyzer.py          # AI-powered video analysis (speech, edits, motion)
│   ├── editor.py            # AI-driven editing logic
│   ├── learner.py           # Learns from user edits (optional for now)
├── processing/
│   ├── video/
│   │   ├── trim.py          # AI-guided trimming (intelligent cuts)
│   │   ├── effects.py       # Transitions, color grading, overlays
│   │   └── render.py        # Final video export logic
│   ├── audio/
│   │   ├── extract.py       # Extracts audio from video
│   │   ├── tts.py           # AI-generated voiceovers (later)
│   │   └── enhance.py       # Noise removal, audio improvement
├── ui/
│   ├── interface.py         # Graphical User Interface (basic for now)
├── data/
│   ├── input/               # User uploads go here
│   ├── processed/           # AI-processed videos before user review
│   ├── output/              # Finalized videos
├── config.json              # User preferences (genre-based settings)
├── requirements.txt         # Dependencies for easy installation
├── README.md                # Documentation
└── main.py                  # Program entry point

Since Python 3.13 is still in development preview and not widely supported, it’s best to downgrade to a stable version.

✅ Recommended Version: Python 3.10.13
Why? Most AI/ML frameworks (PyTorch, TensorFlow, SpeechBrain, etc.) are optimized for Python 3.8 - 3.10.
Better compatibility with libraries like:
    SentencePiece
    SpeechBrain
    NeMo
    FFmpeg, OpenCV, NumPy
    PyTorch CUDA support

🔥 Step-by-Step Setup on Your New PC
1️⃣ Install Python 3.10.13

    Download from: Python 3.10.13 Windows
    ✅ Check the box: "Add Python to PATH" during installation.

2️⃣ Install Virtual Environment
    pip install virtualenv

3️⃣ Create a Virtual Environment for AutoPilot Video Studio
    python -m venv APVS

4️⃣ Activate the Virtual Environment
    APVS\Scripts\activate


5️⃣ Install All Required Dependencies
    pip install -r requirements.txt


🔥 Bonus: Keep Multiple Python Versions
If you need Python 3.13 for other projects, you can use Pyenv or Anaconda to switch between versions.

Install Pyenv (Windows)
iwr -useb https://pyenv.run | Invoke-Expression
Then, install multiple Python versions:
pyenv install 3.10.13
pyenv install 3.13
pyenv global 3.10.13  # Switch to 3.10

🔥 TL;DR: Install Python 3.10.13
Best compatibility with AI tools.
No weird errors with missing dependencies.
Easy CUDA/GPU acceleration for AI video editing.