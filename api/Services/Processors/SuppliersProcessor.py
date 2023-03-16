from threading import Thread, active_count
from Utils.consts import CONSOLE_COLOR, PATHS, ERRORS
from Services.Db.DbService import DbService
from Services.Ftp.FtpConnection import FtpConnection
from SupplierScripts.Hart.Hart import *
from SupplierScripts.Autopartner.Autopartner import *
from SupplierScripts.AutopartnerGdansk.AutopartnerGdansk import *
from SupplierScripts.Emoto.Emoto import *
from SupplierScripts.Gordon.Gordon import *
from SupplierScripts.Motorol.Motorol import *
from SupplierScripts.Paketo.Paketo import *
from SupplierScripts.Rodon.Rodon import *
from SupplierScripts.Motogama.Motogama import *
from SupplierScripts.Elit.Elit import *
from SupplierScripts.InterTeam.InterTeam import *
from SupplierScripts.AutoLand.AutoLand import *
from SupplierScripts.Motoprofil.Motoprofil import *
from SupplierScripts.Intervito.Intervito import *
from SupplierScripts.KrisAuto.KrisAuto import *


#autopartner_to_db()
autopartner_gdansk_to_db()
emoto_to_db()
gordon_to_db()
motorol_to_db()
paketo_to_db()
# hart_to_db()
rodon_to_db()
motogama_to_db()
elit_to_db()
inter_team_to_db()
autoland_to_db()
motorol_to_db()
motoprofil_to_db()
krisauto_to_db()
intervito_to_db()
