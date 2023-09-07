from fastapi import FastAPI

from datetime import datetime, timezone

app = FastAPI()


GITHUB_REPO_URL = "https://github.com/brianobot/zuri_hng_internship"


@app.get("/api")
async def home(slack_name: str = "Brian Obot", track: str = "backend"):
    now = datetime.now()
    return {
        "slack_name": slack_name,
        "current_day": now.strftime("%A"),
        "utc_time": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/brianobot/zuri_hng_internship/blob/master/task_one/main.py",
        "github_repo_url": GITHUB_REPO_URL,
        "status_code": 200,
    }
