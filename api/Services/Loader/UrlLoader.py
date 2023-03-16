import requests as req
import os
from urllib.request import urlopen
import shutil
from contextlib import closing
from Utils.consts import *


def get_file_from_request(supplier, url, file_name):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    resp = req.get(url, headers=user_agent)
    save_folder = os.path.join(PATHS.TEMP_STORAGE, supplier)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    save_path = os.path.join(save_folder, file_name)
    with open(save_path, 'wb') as f:
        f.write(resp.content)

    return save_path


def get_file_from_url(supplier, url, file_name):
    save_folder = os.path.join(PATHS.TEMP_STORAGE, supplier)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    save_path = os.path.join(save_folder, file_name)
    with closing(urlopen(url)) as r:
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(r, f)

    return save_path


class UrlLoader:
    @staticmethod
    def get_file(supplier, url, file_name):
        if url.lower().startswith('ftp://'):
            try:
                print(f'Getting file from FTP URL: {url}')
                return get_file_from_url(supplier, url, file_name)
            except Exception as ex:
                print(f'Exception occurred while getting file!\nURL: {url}\nException: {ex}')
        else:
            try:
                print(f'Getting file with Request: {url}')
                return get_file_from_request(supplier, url, file_name)
            except Exception as ex:
                print(f'Exception occurred while getting file!\nRequest: {url}\nException: {ex}')
