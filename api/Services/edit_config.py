import sys
import ruamel.yaml
from Utils.consts import CONFIG
from Services.load_config import Config


config = Config()

yaml = ruamel.yaml.YAML(typ='safe')
def change_supplier_activity(config, edit_supplier, status):
    config.backup_config()
    suppliers = config.get_app_suppliers()
    with open(CONFIG.CONFIG_LOCATION+CONFIG.CONFIG_NAME) as fp:
        data = yaml.load(fp)
    for supplier in data['suppliers']:
        if supplier['name'] == edit_supplier:
            supplier['status'] = status
    with open(CONFIG.CONFIG_LOCATION+CONFIG.CONFIG_NAME, 'w') as fp:
        yaml.dump(data, fp)
