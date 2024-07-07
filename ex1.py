import queue
import random
import time
import threading

# Створити чергу заявок
request_queue = queue.Queue()

# Функція для генерації унікального ідентифікатора заявки
def generate_request_id():
    return f"REQ-{random.randint(1000, 9999)}"

# Функція для генерації нової заявки
def generate_request():
    request_id = generate_request_id()
    print(f"Generated new request: {request_id}")
    request_queue.put(request_id)

# Функція для обробки заявки
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing request: {request_id}")
        # Імітація часу, необхідного для обробки заявки
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Completed processing request: {request_id}")
    else:
        print("No requests to process. Queue is empty.")

# Головний цикл програми
def main():
    while True:
        # Генерація нових заявок
        generate_request()

        # Обробка заявок
        process_request()

        # Імітація інтервалу між створенням та обробкою заявок
        time.sleep(random.uniform(1.0, 3.0))

# Запуск головного циклу програми у окремому потоці для зручності
if __name__ == "__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()
