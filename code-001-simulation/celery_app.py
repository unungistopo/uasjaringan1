from celery import Celery

#celery CONFIGURATION
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

#create celery instance
celery_app = Celery(
 'project_management',
 broker=CELERY_BROKER_URL,
 backend=CELERY_RESULT_BACKEND,
)

celery_app.conf.broker_connection_retry_on_startup = True

@celery_app.task
def example_task(data:str):
    if not data:
        raise ValueError("Data cannot be empty.")
    return f"Task processed: {data}"

@celery_app.task(queue='pdf_generation')
def generate_schedule_pdf(schedule_data:dict):
    if not schedule_data:
        raise ValueError("Data is required")
    file_name = "schedule.pdf"
    return f"PDF generated: {file_name}"

@celery_app.task(queue='notification')
def send_notification(message:str, recipient:str):
    # Simulate sending a notification
    print(f"Sending notification to {recipient}: {message}")
    return f"Notification sent to {recipient}"

