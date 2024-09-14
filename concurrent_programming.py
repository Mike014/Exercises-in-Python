
import threading
import time

class MyClass:
    def __init__(self):
        pass

    def task1(self):
        for i in range(5):
            print(f"Task 1 - Step {i}")
            time.sleep(1)

    def task2(self):
        for i in range(5):
            print(f"Task 2 - Step {i}")
            time.sleep(1)

    def run_tasks(self):
        # Create threads for task1 and task2
        thread1 = threading.Thread(target=self.task1)
        thread2 = threading.Thread(target=self.task2)

        # Start the threads
        thread1.start()
        thread2.start()

        # Wait for the threads to finish
        thread1.join()
        thread2.join()

# Run the example
if __name__ == "__main__":
    my_instance = MyClass()
    my_instance.run_tasks()


