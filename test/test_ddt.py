import unittest
from util import ddt
import csv


def getCsvData(filepath):
    # 读取CSV文件
    value_rows = []
    with open(filepath, encoding='UTF-8') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
    return value_rows


@ddt.ddt
class MyTestCase(unittest.TestCase):
    data =getCsvData("./login.csv")

    @ddt.data(*data)
    @ddt.unpack
    def test_logindata(self,*data):
        username,password,code=data
        print("用户名是"+username+"密码是:"+password+"验证码是:"+code)
if __name__ == '__main__':
    unittest.main()