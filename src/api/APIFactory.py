from src.api.APIInit import APIInit
from src.api.managepws.ManagePwsController import ManagerPwsController
from src.api.login.LoginController import LoginController

from src.views.RenderClientAssetController import RenderClientAssetController

from src.Config import Config

class APIFactory:

  def __init__(self):
    APIInit.init_flask()
    self.prep_controllers()

  def prep_controllers(self):
    self.manage_pw_controller: ManagerPwsController = ManagerPwsController()
    self.login_controller: LoginController = LoginController()
    self.client_controller: RenderClientAssetController = RenderClientAssetController()

  def run(self):
    context = (f"{Config.root_dir}/example.crt", f"{Config.root_dir}/example.key")
    APIInit.flask.run(host='localhost')