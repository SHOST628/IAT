from util.ddt import TestNameFormat
from util.ddt import ddt, data, unpack
from util.HTMLTestRunner import HTMLTestRunner
import unittest
import time



# @ddt(testNameFormat=TestNameFormat.INDEX_ONLY)
@ddt
class MyTestCase(unittest.TestCase):
    #下面的(1,2)(2,3)代表我们传入的参数,每次传入两个值
    @data([{},{'APINAME':'test','TESTCASEID':'TC01'}], [{},{'APINAME':'test','TESTCASEID':'TC02'}])
    #告诉我们的测试用例传入的是两个以上的值
    @unpack
    #定义两个参数value用于接收我们传入的参数
    def test_something(self,value1,value2):
        print(value1,value2)
        #对于传入的第一个参数+1与第二个参数进行对比,相等就通过,否则就是不通过
        # self.assertEqual(value2, value1+1)


if __name__ == '__main__':
    ts = unittest.TestSuite()
    loader = unittest.TestLoader()
    ts.addTest(loader.loadTestsFromTestCase(MyTestCase))
    # now = time.strftime("%m%d_%H_%M_%S",time.localtime(time.time()))
    with open('report.html', 'wb') as f:
        runner = HTMLTestRunner(
            stream = f,
            verbosity = 2,
            title="测试报告",
            description='TestReport'
        )
        runner.run(ts)