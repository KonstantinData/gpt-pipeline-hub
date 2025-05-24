# main.py (FastAPI WebUI for eval pipeline)

from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess
from pathlib import Path
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

EVAL_DIR = Path("evals")
SUMMARY_FILE = EVAL_DIR / "pipeline_summary.json"
COST_FILE = EVAL_DIR / "token_costs_summary.json"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    summary_data = {}
    if SUMMARY_FILE.exists():
        with open(SUMMARY_FILE, encoding="utf-8") as f:
            summary_data = json.load(f)
    return templates.TemplateResponse(
        "index.html", {"request": request, "summary": summary_data}
    )


@app.post("/run")
def run_pipeline(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_all)
    return {"status": "⏳ Evaluation started in background"}


def run_all():
    subprocess.run(["python", "eval_chain.py"], check=True)
    subprocess.run(["python", "token_cost_summary.py"], check=True)


@app.get("/download/{filename}")
def download_result(filename: str):
    file_path = EVAL_DIR / filename
    if file_path.exists():
        return FileResponse(file_path, filename=filename)
    return {"error": "File not found"}
