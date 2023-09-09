import unittest

class ParameterizedTestCase(unittest.TestCase):
    """
    重构 unittest.TestCase，加载 测试用例时，能把用例需要的参数传递进去
    """
    def __init__(self,methodName="runTest",param=None):
        super(ParameterizedTestCase,self).__init__(methodName)
        # 指定启动哪台设备
        self.serial_number = param

    # 静态方法
    @staticmethod
    def parameterized(testcase_klass,args=None):
        """
        :param testcase_klass: 测试用例所在类，然后在这个类中寻找 prefix=self.testMethodPrefix(test)开头的测试用例
        :param args: 加载测试类中的用例，并把参数传递给测试类，会把args传递给 unittest 框架的 __init__ 函数
        :return:
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()

        for name in testnames:
            # 这里的 param 必须是 __init__ 函数中的形参
            suite.addTest(testcase_klass(name,param=args))

        return suite
