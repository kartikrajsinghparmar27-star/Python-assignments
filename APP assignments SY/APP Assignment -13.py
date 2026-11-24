import threading
import time

# Task 1
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Task 2
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", letter)
        time.sleep(1)

# Task 3
def print_message():
    for i in range(5):
        print("Hello from Thread 3")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=print_message)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("All threads completed.")