#coding=utf-8

import os
import traceback
import unittest
from config import ymlConfig
import HTMLTestRunner
from logger import log

class runTest(object):

    project_path = os.path.abspath(os.path.join(os.getcwd(), "."))

    def __init__(self):
        self.yml = ymlConfig.YmlConfig()
        self.logger = log.Log()

        self.report_path = self.project_path + self.yml.read_vars('report')
        self.test_case_path = self.project_path + self.yml.read_vars('case')

    def get_suite(self):
        suite = unittest.TestSuite()   # 创建测试套件
        all_cases = unittest.defaultTestLoader.discover(start_dir=self.test_case_path, pattern='test*.py')
        # 找到某个目录下所有的以test开头的python文件里面的测试用例
        for case in all_cases:
            suite.addTests(case)  # 把所有的测试用例添加进来
        return suite
    '''
         def clear_report_files(self):
            try:
                # remove last report file
                for rm_file in os.listdir(self.report_path): 
                    target = os.path.join(self.report_path, rm_file)
                    if os.path.isfile(target):
                        os.remove(target)
            except Exception:
                print traceback.print_exc()
    '''
    def generate_reports(self, test_suite):
        report = self.report_path + 'TestReport.html'
        fp = open(report, 'w')
        self.logger.info('start runing test suite ...')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'SSO接口测试报告',
                                               description=u'SSO接口测试用例执行情况')
        runner.run(test_suite)
        fp.close()


if __name__ == '__main__':
    try:
        test = runTest()
        test.generate_reports(test.get_suite())
    except Exception:
        print(traceback.print_exc())
