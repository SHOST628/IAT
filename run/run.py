from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, FIRST_COMPLETED
import os
import sys
import threading
sys.path.append(os.path.dirname(__file__))


class CaseCollection(threading.Thread):
    def __init__(self, queue, nloop, condition):
        super().__init__()
        self.condition = condition
        self.queue = queue
        self.nloop = nloop

    def write_queue(self, item):
        self.queue.put(item)
        print("put item: {}".format(item))

    def run(self):
        with self.condition:
            for i in range(self.nloop):
                self.write_queue(i)
                self.condition.notify()
                self.condition.wait()
                if i == self.nloop - 1:
                    self.queue.put(None)
                    self.condition.notify()


class Execution(threading.Thread):
    def __init__(self, queue, condition):
        super().__init__()
        self.queue = queue
        self.condition = condition

    def read_queue(self):
        res = self.queue.get()
        if res is not None:
            print("current thread {} get: {}".format(threading.current_thread().name, res))
            return 0
        else:
            return None

    def run(self):
        while True:
            with self.condition:
                self.condition.wait()
                res = self.read_queue()
                if res is None:
                    break
                self.condition.notify()


def run_case():
    """exectue all testcase"""
    # report_path = ReadConfig().get_report_path("path")
    # email = Email()
    # email.send_email()
    data_queue = Queue()
    condition = threading.Condition()
    case_collection = CaseCollection(data_queue, 100, condition)
    execution = Execution(data_queue, condition)
    execution.start()
    case_collection.start()


if __name__ == "__main__":
    run_case()
