from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, FIRST_COMPLETED
import threading
q = Queue()
for item in range(1000):
    q.put(item)
    if item == 999:
        q.put(None)


def get_data(q):
    res = q.get()
    print(res)
    return res


with ThreadPoolExecutor(3) as executor:
    # with threading.Condition() as con:
    all_task = [executor.submit(get_data, q) for i in range(1001)]
    wait(all_task,return_when=FIRST_COMPLETED)
    tasks = as_completed(all_task)
    for task in tasks:
        if task is None:
            break


