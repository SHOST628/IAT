from queue import Queue
import threading
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
TASK_QUEUE = Queue()
for item in range(1,10):
    TASK_QUEUE.put(item)
    if item == 9:
        TASK_QUEUE.put(None)
con = threading.Condition()


def get_job(q):
    item = q.get()
    return item


def put_job(temp_queue, item):
    res = item.get()
    temp_queue.put(res)
    if res is None:
        return res

def t_put(put_job, temp_queue):
    global TASK_QUEUE
    with ThreadPoolExecutor(3) as executor:
        while True:
            res = executor.submit(put_job, temp_queue, TASK_QUEUE)
            result = res.result()
            if result is None:
                break
            print("put item: {}".format(result))

def t_get(get_job, tmep_queue):
    with ThreadPoolExecutor(2) as executor:
        while True:
            if not tmep_queue.empty():
                res = executor.submit(get_job, tmep_queue)
                result = res.result()
                if result is None:
                    break
            print("get item: {}".format(result))


temp_queue = Queue()
th_put = threading.Thread(target=t_put, args=(put_job, TASK_QUEUE))
th_get = threading.Thread(target=t_get, args=(get_job, temp_queue))
th_put.start()
th_get.start()
th_put.join()
th_get.join()
print("done\n")