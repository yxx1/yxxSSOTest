#coding=utf-8
import os
import traceback
import yaml
from logger import log


class YmlConfig(object):
    def __init__(self):
        self.logger = log.Log()

    def read_vars(self, var_name):
        try:
            config_path = os.path.abspath(os.path.dirname(__file__))+r'\config.yml'
            configfile = open(config_path)
            cont = configfile.read()
            res = yaml.load(cont, Loader=yaml.FullLoader)
            var_value = res[var_name]
            return var_value
        except Exception:
            self.logger.error(traceback.print_exc())













