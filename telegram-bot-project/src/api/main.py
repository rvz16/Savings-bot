from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Telegram Bot API"}

@app.post("/topics/")
def create_topic(topic: str):
    # Logic to save the topic
    return {"message": f"Topic '{topic}' created successfully."}

@app.get("/reminders/")
def get_reminders():
    # Logic to retrieve video reminders
    return {"reminders": []}

@app.post("/videos/")
def save_video(video_url: str, importance_level: int):
    # Logic to save the video with importance level
    return {"message": f"Video '{video_url}' saved with importance level {importance_level}."}