from fastapi import FastAPI

from datetime import datetime ,timezone

app = FastAPI()


@app.get("/api")
async def read_root(slack_name: str = "Brian Obot", track: str = "backend"):
    now = datetime.now()
    return {
        "slack_name": slack_name,
        "current_day": now.strftime("%A"),
        "utc_time": datetime.now(timezone.utc),
        "track": track,
        "github_file_url": "https://github.com/brianobot/zuri_hng_internship/blob/master/task_one/main.py",
        "github_repo_url": "https://github.com/brianobot/zuri_hng_internship",
        "status_code": 200,
    }
