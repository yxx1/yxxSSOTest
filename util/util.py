#coding=utf-8
import json
import traceback
import requests
import xlrd
from config import ymlConfig
from logger import log
import pymysql


class Util:

    def __init__(self):
        self.logger = log.Log()
        self.config = ymlConfig.YmlConfig()

        self.mysqlHost = self.getProperties('mysqlHost')
        self.mysqlPort = self.getProperties('mysqlPort')
        self.mysqlDatabase = self.getProperties('mysqlDatabase')
        self.mysqLUserName = self.getProperties('mysqLUserName')
        self.mysqlPassWord = self.getProperties('mysqlPassWord')

    # 读取excel表格中的一行数据
    def read_excel_row(self, test_name):
        try:
            #打开指定位置的excel
            excelFile = xlrd.open_workbook(r'D:\python_work\SSOTest\util\test.xlsx')
            # 根据索引的方式，打开第一个sheet页
            sheet = excelFile.sheet_by_index(0)
            #根据sheet的名字获取
            #excelFile.sheet_by_name('name')
            nrows = sheet.nrows #行数
            ncols = sheet.ncols #列数
            result = []
            for row in range(0, nrows):
                if sheet.row(row)[0].value == test_name:
                    for col in range(0, ncols):
                        value = sheet.row(row)[col].value.encode('utf-8')
                        result.append(value)
                    break
            return result
        except Exception:
            self.logger.error(traceback.print_exc())

    # HTTP/HTTPS的请求
    def send_request(self, url, method, data_dic):
        try:
            # 设置请求头
            headers = {'accept': '*/*',
                       'connection': 'Keep-Alive',
                       'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'}
            if method == 'GET':
                # 发送get请求
                r = requests.get(url, params=data_dic, headers=headers)
                return r.text.encode('utf-8')
            elif method == 'POST':
                # 发送post请求
                r = requests.post(url, data=data_dic, headers=headers)
                return r.text.encode('utf-8')
        except Exception:
            self.logger.error(traceback.print_exc())

    # 对请求的返回字符串进行assert判定；与excel表中提供的检查数据进行assertEquals判断
    def assert_result(self, base_url, test_name):
        try:
            # 读取excel的一行数据
            data_list = self.read_excel_row(test_name)
            # 拼接完整url
            url = base_url + data_list[1]
            # method,获取传输方式get/post
            method = data_list[2]
            # 参数
            data_str = data_list[3]
            # str转成字典
            data_dic = json.loads(data_str)
            reponse_list = data_list[4].split(',')
            # 发送请求
            response = self.send_request(url, method, data_dic)

            # 遍历Excel中的预期响应
            for i in range(len(reponse_list)):
                # 判断实际响应数据是否包含Excel中预期响应数据
                if reponse_list[i] in response:
                    flag = True
                else:
                    flag = False
            return flag
        except Exception:
            self.logger.error(traceback.print_exc())
            return False

    # 对请求的返回字符串进行assert判定；与excel表中提供的检查数据进行assertEquals判断,动态传入hxut
    def assert_result_hxut(self, base_url, test_name, hxut):
        try:
            # 读取excel的一行数据
            data_list = self.read_excel_row(test_name)
            # 拼接完整url
            url = base_url + data_list[1]
            # method,获取传输方式get/post
            method = data_list[2]
            # 参数
            data_str = data_list[3].replace('huanxi', hxut)
            # str转成字典
            data_dic = json.loads(data_str)
            reponse_list = data_list[4].split(',')
            # 发送请求
            response = self.send_request(url, method, data_dic)

            # 遍历Excel中的预期响应
            for i in range(len(reponse_list)):
                # 判断实际响应数据是否包含Excel中预期响应数据
                if reponse_list[i] in response:
                    flag = True
                else:
                    flag = False
            return flag
        except Exception:
            self.logger.error(traceback.print_exc())
            return False

    # 读取yml中的配置信息
    def getProperties(self, var_name):
        try:
            var_name = self.config.read_vars(var_name)
            return var_name
        except Exception:
            self.logger.error(traceback.print_exc())


    # # 获取reset pwd时的uid的值，默认账号是16619884679/123456
    # def get_uid(self):
    #     try:
    #         response_str = self.send_request(self.getProperties('verifyURL'), self.getProperties('Method1'), self.getProperties('verifyParam'))
    #         response_dic = json.loads(response_str)
    #         uid = response_dic['result']['rud']
    #         return uid
    #     except Exception:
    #         self.logger.error(traceback.print_exc())
    #
    # # 查询数据库
    # def sql_query(self, sqlCommand):
    #     try:
    #         # 链接数据库
    #         conn = pymysql.connect(host=self.mysqlHost, port=self.mysqlPort, user=self.mysqLUserName, password=self.mysqlPassWord, database=self.mysqlDatabase, charset='utf8')
    #         # 获取一个光标，等待输入sql语句
    #         cursor = conn.cursor()
    #         # 执行sql语句
    #         result = cursor.execute(sqlCommand)
    #         print result
    #         # 关闭光标对象
    #         cursor.close()
    #         # 关闭数据库链接
    #         conn.close()
    #     except Exception as e:
    #         self.logger.error(traceback.print_exc())
    #
    # # 查询数据库
    # def sql_update(self, sqlCommand):
    #     # 链接数据库
    #     conn = pymysql.connect(host=self.mysqlHost, port=self.mysqlPort, user=self.mysqLUserName,
    #                            password=self.mysqlPassWord, database=self.mysqlDatabase, charset='utf8')
    #     # 获取一个光标，等待输入sql语句
    #     cursor = conn.cursor()
    #     try:
    #         # 执行sql语句
    #         result = cursor.execute(sqlCommand)
    #         print result
    #         # 写操作注意提交
    #         conn.commit()
    #     except Exception as e:
    #         # 有异常，回滚事务
    #         conn.rollback()
    #         self.logger.error(traceback.print_exc())
    #     # 关闭光标对象
    #     cursor.close()
    #     # 关闭数据库链接
    #     conn.close()











