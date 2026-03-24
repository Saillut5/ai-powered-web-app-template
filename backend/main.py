from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Dummy AI model for demonstration
class DummyAIModel:
    def predict(self, text: str) -> str:
        if "hello" in text.lower():
            return "AI: Hello there! How can I help you today?"
        elif "weather" in text.lower():
            return "AI: I'm sorry, I don't have access to real-time weather data."
        elif "sad" in text.lower():
            return "AI: I'm sorry to hear that. Is there anything I can do to cheer you up?"
        else:
            return f"AI: You said: \"{text}\". I am a dummy AI and can only respond to a few keywords."

app = FastAPI()
ai_model = DummyAIModel()

class TextInput(BaseModel:
    text: str

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "Backend is running"}

@app.post("/api/predict")
async def predict_text(input: TextInput):
    try:
        prediction = ai_model.predict(input.text)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
