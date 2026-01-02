# EmoDetect - Real-time Emotion Analysis

EmoDetect is a cutting-edge web application that leverages advanced AI to detect and analyze human emotions in real-time. Built with a modern tech stack, it provides instant visual feedback, comprehensive session analytics, and professional PDF reporting.

## 🚀 Features

- **Real-time Emotion Recognition**: Uses DeepFace to analyze facial expressions with high accuracy.
- **Dynamic Analytics Dashboard**: Visualizes emotion trends, dominant emotions, and confidence levels.
- **Session Recording**: Capture video and audio of your analysis sessions.
- **PDF Reporting**: Generate professional reports with detailed insights and charts.
- **Modern UI/UX**: A dark-themed, glassmorphic interface designed for immersion and ease of use.

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla CSS, JavaScript
- **Video/Audio**: AgoraRTC SDK for real-time media handling
- **Backend**: Python (FastAPI)
- **AI Model**: DeepFace (TensorFlow/Keras)
- **Reporting**: fpdf2 for PDF generation
- **Charts**: Chart.js

## 📦 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/emodetect.git
    cd emodetect
    ```

2.  **Backend Setup**
    Navigate to the `back-end` directory and set up the Python environment:
    ```bash
    cd back-end
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  **Frontend Setup**
    The frontend is a static site. You can serve it using `npx serve` or any static file server.
    ```bash
    cd ../
    npx serve frontend
    ```

4.  **Running the Application**
    - **Backend**: `uvicorn back-end.main:app --reload` (runs on http://127.0.0.1:8000)
    - **Frontend**: Open the URL provided by `npx serve` (usually http://localhost:3000)

## 🔮 Roadmap

- [ ] **Multi-modal Analysis**: Incorporate voice tone analysis for richer emotional context.
- [ ] **Attention Tracking**: Monitor user gaze and attention levels.
- [ ] **User Accounts**: Persist session history and reports in the cloud.

## 📄 License

This project is licensed under the MIT License.
