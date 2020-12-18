from util.ddt import ddt
from util.ddt import data
from util.ddt import unpack
import unittest


@ddt
class DemoTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data()
    def test_something(self):
        pass