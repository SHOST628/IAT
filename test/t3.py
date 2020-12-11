import threading
from threading import Condition


class XiaoMing(threading.Thread):
    def __init__(self, condition):
        super().__init__(name='小明')
        self.condition = condition

    def run(self):
        with self.condition:
            print('{}:小红'.format(self.name))
            self.condition.notify()
            self.condition.wait()

            print('{}:我喜欢你'.format(self.name))
            self.condition.notify()
            self.condition.wait()


class XiaoHong(threading.Thread):
    def __init__(self, condition):
        super().__init__(name='小红')
        self.condition = condition

    def run(self):
        with self.condition:
            self.condition.wait()
            print('{}:在'.format(self.name))
            self.condition.notify()

            self.condition.wait()
            print('{}:对不起,你是个好人'.format(self.name))
            self.condition.notify()


if __name__ == '__main__':
    condition = threading.Condition()
    xiaoming = XiaoMing(condition)
    xiaohong = XiaoHong(condition)

    xiaohong.start()
    xiaoming.start()