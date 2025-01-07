# celery_app.py
from celery import Celery

# Inisialisasi aplikasi Celery
celery_app = Celery(
    'project_management',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
)

# Konfigurasi Celery
celery_app.conf.broker_connection_retry_on_startup = True

@celery_app.task(queue='pdf_generation')
def generate_schedule_pdf(schedule_data):
    if not schedule_data:
        raise ValueError("Data is required")
    # Simulasi pembuatan PDF
    file_name = "schedule.pdf"
    # Di sini seharusnya ada logika pembuatan PDF sebenarnya
    return f"PDF generated: {file_name}"

@celery_app.task(queue='notification')
def send_notification(message: str, recipient: str):
    # Simulasi pengiriman notifikasi
    print(f"Sending notification to {recipient}: {message}")
    return f"Notification sent to {recipient}"

@celery_app.task(queue='data_update')
def update_project_status(project_id, status):
    # Simulasi pembaruan status proyek di database
    print(f"Updating project {project_id} to status: {status}")
    return f"Project {project_id} updated to {status}"

@celery_app.task(queue='archiving')
def archive_old_projects(project_ids):
    # Simulasi proses pengarsipan proyek
    archived = []
    for project_id in project_ids:
        print(f"Archiving project: {project_id}")
        archived.append(project_id)
    return f"Archived projects: {archived}"

@celery_app.task
def example_task(data):
    return f"Task processed: {data}"

@celery_app.task
def generate_pdf(project_data):
    import time
    time.sleep(5)  # Simulasi proses yang memakan waktu
    file_name = f"{project_data['nama_proyek']}_schedule.pdf"
    with open(file_name, 'w') as f:
        f.write(f"Schedule for: {project_data['nama_proyek']}")
    return {"status": "completed", "file_name": file_name}
