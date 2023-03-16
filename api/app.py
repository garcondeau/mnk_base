from flask import Flask, request
from SupplierScripts.Paketo.Paketo import paketo_to_db
from SupplierScripts.AutopartnerGdansk.AutopartnerGdansk import autopartner_gdansk_to_db
from Services.load_config import Config
from Services.edit_config import change_supplier_activity
from Utils.consts import CONFIG


app = Flask(__name__)
config = Config()
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)


@app.route('/app-info')
def get_app_info():
    return config.get_app_info()


@app.route('/suppliers/<supplier>')
def supplier_details(supplier):
    if request.method == 'POST':
        pass
    else:
        config = Config()
        return config.get_supplier_by_name(supplier)

@app.route('/suppliers', methods=['POST', 'GET'])
def get_suppliers():
    if request.method == 'POST':
        data = request.get_json()
        change_supplier_activity(config=config, edit_supplier=data['supplier'], status=data['status'])
        print(data)
        return data
    else:
        return config.get_app_suppliers()

app.run(extra_files=[f'./Utils\\{CONFIG.CONFIG_NAME}'])