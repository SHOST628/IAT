import os,sys
import random
sys.path.append(os.path.dirname(__file__))
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, FIRST_COMPLETED
import threading


def write_queue(queue, item):
    queue.put(item)
    print("put item: {}".format(item))


def read_queue(queue):
    res = queue.get()
    if res is not None:
        print("current thread {} get: {}".format(threading.current_thread().name, res))
    return res


def writer(queue, condition):
    with condition:
        for i in range(20000):
            write_queue(queue, i)
            condition.notify()
            condition.wait()
            if i == 19999:
                queue.put(None)
                condition.notify()


def reader(queue, read_queue, condition):
    with ThreadPoolExecutor(3) as executor:
        while True:
            with condition:
                condition.wait()
                task = executor.submit(read_queue, queue)
                if task.result() is None:
                    break
                condition.notify()


def run_case():
    """exectue all testcase"""
    # report_path = ReadConfig().get_report_path("path")
    # email = Email()
    # email.send_email()
    data_queue = Queue()
    condition = threading.Condition()
    th_writer = threading.Thread(target=writer, args=(data_queue, condition))
    th_reader = threading.Thread(target=reader, args=(data_queue, read_queue, condition))
    th_reader.start()
    th_writer.start()


if __name__ =="__main__":
    run_case()
