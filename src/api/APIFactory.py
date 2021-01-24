from src.api.APIInit import APIInit
from src.api.managepws.ManagePwsController import ManagerPwsController
from src.api.login.LoginController import LoginController

from src.views.RenderHTML import RenderHTML
from src.views.RenderJS import RenderJS

from src.Config import Config
from src.util.networking.IP import IPHelpers

class APIFactory:

  def __init__(self):
    APIInit.init_flask()
    self.prep_controllers()

  def prep_controllers(self):
    self.manage_pw_controller: ManagerPwsController = ManagerPwsController()
    self.login_controller: LoginController = LoginController()

    RenderJS.init_js_conf()

    self.html: RenderHTML = RenderHTML()
    self.js: RenderJS = RenderJS()

  def run(self):
    context = (f"{Config.root_dir}/example.crt", f"{Config.root_dir}/example.key")
    APIInit.flask.run(host='localhost')