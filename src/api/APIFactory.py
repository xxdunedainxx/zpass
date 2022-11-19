from src.api.APIInit import APIInit
from src.api.managepws.ManagePwsController import ManagerPwsController
from src.api.login.LoginController import LoginController
from src.api.monitoring.MonitoringController import MonitoringController

from src.views.RenderClientAssetController import RenderClientAssetController
from src.util.networking.IP import IPHelpers

from src.Config import Config

class APIFactory:

  def __init__(self):
    APIInit.init_flask()
    self.prep_controllers()

  def prep_controllers(self):
    self.manage_pw_controller: ManagerPwsController = ManagerPwsController()
    self.login_controller: LoginController = LoginController()
    self.client_controller: RenderClientAssetController = RenderClientAssetController()
    self.monitoring_controller: MonitoringController = MonitoringController()

  def run(self):
    context = (f"{Config.root_dir}/example.crt", f"{Config.root_dir}/example.key")
    APIInit.flask.run(host=IPHelpers.my_ip())