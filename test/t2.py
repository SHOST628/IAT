import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


class ThreadPool (object):
    def __init__(self):
        pass

    def get_data(self):
        sleep = random.randint (1, 10)
        return sleep

    def start(self):
        all_code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        executor = ThreadPoolExecutor(4)
        all_task = [executor.submit(self.get_data) for code in all_code]
        wait(all_task, return_when=FIRST_COMPLETED)
        for future in as_completed(all_task):
            data = future.result()
            print(data)

    def run(self):
        self.start()


if __name__ == '__main__':
    tp = ThreadPool()
    tp.run()