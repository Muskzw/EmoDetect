from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from deepface import DeepFace
import cv2
import numpy as np
import os
import tempfile

app = FastAPI()

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "EmoDetect AI API is active (DeepFace)"}

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    # Save the uploaded file to a temporary location
    temp_fd, temp_path = tempfile.mkstemp(suffix=".jpg")
    try:
        contents = await file.read()
        with os.fdopen(temp_fd, 'wb') as tmp:
            tmp.write(contents)
        
        # Analyze the image for emotions using DeepFace
        # enforce_detection=False prevents crash if no face is found
        results = DeepFace.analyze(
            img_path=temp_path, 
            actions=['emotion'],
            enforce_detection=False,
            detector_backend='opencv' # Fastest for real-time
        )
        
        # DeepFace returns a list of results (one for each face detected)
        if results and len(results) > 0:
            dominant_emotion = results[0]['dominant_emotion'].capitalize()
            
            # Map to frontend expected labels
            mappings = {
                "Surprise": "Surprised",
                "Disgust": "Disgusted"
            }
            dominant_emotion = mappings.get(dominant_emotion, dominant_emotion)
            
            confidence = int(results[0]['emotion'][results[0]['dominant_emotion']])
            
            print(f"Detected: {dominant_emotion} ({confidence}%)")
            return [dominant_emotion, confidence]
        
        return ["Neutral", 0] # Fallback if no face detected

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return ["Neutral", 0]
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    import uvicorn
    # Pre-load the model to avoid delay on first request
    print("Starting server...")
    # try:
    #     DeepFace.build_model("Emotion")
    # except:
    #     pass
    uvicorn.run(app, host="0.0.0.0", port=8000)
