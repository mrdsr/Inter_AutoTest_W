import unittest

from HtmlTestRunner import HTMLTestRunner
import logging
class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类执行之前的方法")

    @classmethod
    def tearDownClass(cls):
        print("类执行之后的方法")

    def setUp(self):
        print('每次方法之前执行')

    def tearDown(self):
        print('每次方法之后执行')

    def test_01(self):
        # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # logger = logging.getLogger(__name__)
        # logger.info("Start logger output")
        # logger.debug("data message wrong")
        # logger.warning("数据可能会丢失,网络不稳定")
        # logger.info("----------------Test finsh")
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.DEBUG)
        handle = logging.FileHandler("log.txt")
        handle.setLevel(level=logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handle.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logger.addHandler(console)
        logger.addHandler(handle)
        logger.info("infodebug")
        logger.debug("woshi debug")
        logger.warning("wozhaobudaogongzuo")

        print("1")

    def test_02(self):
        print("2")

    def test_03(self):
        print("3")


if __name__ == '__main__':
    filepath = "htmlreport.html"
    fp = open(filepath,"wb")
    #构造用例集
    suite = unittest.TestSuite()
    #添加用例
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_03'))
    # suite.addTest(TestMethod('test_02'))

    runner = HTMLTestRunner(stream=fp,title="this is first report")
    #执行测试
    runner.run(suite)
    fp.close()
