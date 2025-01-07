from celery_app import example_task, generate_schedule_pdf, send_notification
import time

def run_example_task():
    print("Running example_task...")
    # Kirim tugas example_task
    result = example_task.delay("Sample data for example_task")
    print(f"Task ID: {result.id}")
    # Tunggu hingga selesai
    while not result.ready():
        print("Waiting for example_task to complete...")
        time.sleep(1)
    print(f"Result: {result.get()}")

def run_generate_schedule_pdf():
    print("Running generate_schedule_pdf...")
    # Kirim tugas generate_schedule_pdf
    schedule_data = {"event": "Meeting", "date": "2025-01-08", "time": "10:00 AM"}
    result = generate_schedule_pdf.delay(schedule_data)
    print(f"Task ID: {result.id}")
    # Tunggu hingga selesai
    while not result.ready():
        print("Waiting for generate_schedule_pdf to complete...")
        time.sleep(1)
    print(f"Result: {result.get()}")

def run_send_notification():
    print("Running send_notification...")
    # Kirim tugas send_notification
    message = "Hello! Your schedule is ready."
    recipient = "user@example.com"
    result = send_notification.delay(message, recipient)
    print(f"Task ID: {result.id}")
    # Tunggu hingga selesai
    while not result.ready():
        print("Waiting for send_notification to complete...")
        time.sleep(1)
    print(f"Result: {result.get()}")

if __name__ == "__main__":
    print("Select a task to run:")
    print("1. Run example_task")
    print("2. Run generate_schedule_pdf")
    print("3. Run send_notification")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        run_example_task()
    elif choice == "2":
        run_generate_schedule_pdf()
    elif choice == "3":
        run_send_notification()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
