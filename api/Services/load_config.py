import os
import io
from time import time
import yaml
import shutil
from datetime import date, time, datetime
from Utils.consts import CONFIG, CONSOLE_COLOR


def check_supplier_status(status):
    if status == True:
        return 'Enabled'
    else:
        return 'Disabled'


class Config:
    def __init__(self):
        self.config_data = ''
        with open(CONFIG.CONFIG_LOCATION+CONFIG.CONFIG_NAME, 'r') as stream:
            self.config_data = yaml.safe_load(stream)

    def get_app_info(self):
        if 'version' in self.config_data:
            app_version = self.config_data.get('version')
        else:
            app_version = 'undefined version'
        if 'build' in self.config_data:
            app_build = self.config_data.get('build')
        else:
            app_build = 'undefined build'
        return [app_build, app_version]

    def get_app_suppliers(self):
        suppliers_dict = self.config_data.get('suppliers')
        return suppliers_dict

    def backup_config(self):
        backup_path = CONFIG.CONFIG_LOCATION + \
            f'backup/{datetime.timestamp(datetime.now())}/'
        isExist = os.path.exists(backup_path)
        if not isExist:
            os.makedirs(backup_path)
        config_backup = f'{backup_path}/{CONFIG.CONFIG_NAME}'
        shutil.copy(CONFIG.CONFIG_LOCATION+CONFIG.CONFIG_NAME, config_backup)
        print(f'{CONSOLE_COLOR.WARNING}!!! YOUR CONFIG BACKUP WAS CREATED AND IS LOCATED IN {CONSOLE_COLOR.HEADER}{config_backup}{CONSOLE_COLOR.WARNING} !!!{CONSOLE_COLOR.NC}')

    def get_supplier_by_name (self, supplier_name):
        config = Config()
        suppliers_list = config.get_app_suppliers()
        supplier = {}
        for sup in suppliers_list:
            if sup['name'] == supplier_name:
                supplier = sup
        return supplier


