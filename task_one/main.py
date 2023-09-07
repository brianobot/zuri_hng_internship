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
        "github_file_url": "sdfisdofsniofsdnofsdf",
        "github_repo_url": "snfsidnfsuifsnfsndfisdf",
        "status_code": 200,
    }
