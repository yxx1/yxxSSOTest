#coding=utf-8
import unittest
from logger import log
from util import util
import traceback

class AppSsoTest(unittest.TestCase):
    UTIL = util.Util()
    logger = log.Log()

    @classmethod
    def setUpClass(cls):
        cls.logger.info('Into AppSsoTest setUpClass ...')
        cls.SSO_AAP_URL = cls.UTIL.getProperties('SSO_APP_URL')

    # phone、pwd参数输入空值（两者都为空、分别为空）
    def testLogin1(self):
        u"""phone、pwd参数输入空值（两者都为空、分别为空）"""
        self.logger.info('Into testLogin1 ...')
        testName = 'testLogin1'
        try:
            if self.UTIL.assert_result(self.SSO_AAP_URL, testName):
                self.logger.info(testName + ' PASS')
                self.assertTrue(True)
            else:
                self.logger.error(testName + ' FAIL')
                self.assertFalse(False)
        except Exception:
            self.logger.error(traceback.print_exc())

    # phone不足11位
    def testLogin2(self):
        u"""phone不足11位"""
        self.logger.info('Into testLogin2 ...')
        testName = 'testLogin2'
        try:
            if self.UTIL.assert_result(self.SSO_AAP_URL, testName):
                self.logger.info(testName + ' PASS')
                self.assertTrue(True)
            else:
                self.logger.error(testName + ' FAIL')
                self.assertFalse(False)
        except Exception:
            self.logger.error(traceback.print_exc())

