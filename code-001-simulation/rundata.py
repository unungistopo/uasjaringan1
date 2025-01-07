from celery_app import generate_schedule_pdf, send_notification

# Menambahkan tugas generate PDF ke antrian
result_pdf = generate_schedule_pdf.delay([
    {'date': '2025-01-10', 'task': 'Kickoff Meeting'},
    {'date': '2025-01-15', 'task': 'Requirement Gathering'}
])

# Memastikan bahwa send_notification mendukung argumen message dan recipient
result_notification = send_notification.delay(
    {"message": "Early warning: Deadline approaching!", "recipient": "team@example.com"}
)

# Menampilkan ID tugas yang ditambahkan ke antrian
print("Task IDs:", result_pdf.id, result_notification.id)
