# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_app import example_task, generate_schedule_pdf, send_notification
from celery_app import celery_app

app = FastAPI()

# Model untuk request body pada /create_task
class TaskCreateRequest(BaseModel):
    data: dict

# Model untuk request body pada /create_pdf_task
class PdfTaskCreateRequest(BaseModel):
    schedule_data: list

# Model untuk request body pada /send_notification_task
class NotificationTaskCreateRequest(BaseModel):
    message: str
    recipient: str

@app.post("/create_task")
async def create_task(request: TaskCreateRequest):
    task = example_task.delay(request.data)
    return {"task_id": task.id, "status": "Task added to the queue"}

@app.post("/create_pdf_task")
async def create_pdf_task(request: PdfTaskCreateRequest):
    task = generate_schedule_pdf.delay(request.schedule_data)
    return {"task_id": task.id, "status": "PDF Task added to the queue"}

@app.post("/send_notification_task")
async def send_notification_task(request: NotificationTaskCreateRequest):
    task = send_notification.delay(request.message, request.recipient)
    return {"task_id": task.id, "status": "Notification Task added to the queue"}

@app.get("/task_status/{task_id}")
async def get_task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task_id": task_id, "status": result.status, "result": result.result}
