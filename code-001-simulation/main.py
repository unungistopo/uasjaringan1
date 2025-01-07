from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_app import example_task, generate_schedule_pdf, send_notification

app = FastAPI()

# Pydantic model untuk validasi data
class ExampleTaskData(BaseModel):
    data: str

class ScheduleData(BaseModel):
    event: str
    date: str
    time: str

class NotificationData(BaseModel):
    message: str
    recipient: str

@app.post("/run_example_task")
async def run_example_task(task_data: ExampleTaskData):
    result = example_task.delay(task_data.data)
    return JSONResponse(content={"task_id": result.id, "status": "Task submitted"})

@app.post("/run_generate_schedule_pdf")
async def run_generate_schedule_pdf(schedule_data: ScheduleData):
    result = generate_schedule_pdf.delay(schedule_data.dict())
    return JSONResponse(content={"task_id": result.id, "status": "Task submitted"})

@app.post("/run_send_notification")
async def run_send_notification(notification_data: NotificationData):
    result = send_notification.delay(notification_data.message, notification_data.recipient)
    return JSONResponse(content={"task_id": result.id, "status": "Task submitted"})

@app.get("/task_status/{task_id}")
async def task_status(task_id: str):
    # Mendapatkan status task berdasarkan ID
    result = AsyncResult(task_id)

    # Cek status task
    if result.state == "PENDING":
        return JSONResponse(content={"task_id": task_id, "status": "PENDING", "message": "Task is pending or unknown."})
    elif result.state == "SUCCESS":
        return JSONResponse(content={"task_id": task_id, "status": "SUCCESS", "result": result.result})
    elif result.state == "FAILURE":
        return JSONResponse(content={"task_id": task_id, "status": "FAILED", "message": str(result.info)})
    else:
        return JSONResponse(content={"task_id": task_id, "status": result.state, "message": "Task is in progress or has a different state."})
