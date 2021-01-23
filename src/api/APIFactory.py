from src.api.APIInit import APIInit
from src.api.managepws.ManagePwsController import ManagerPwsController
from src.api.login.LoginController import LoginController
class APIFactory:

  def __init__(self):
    APIInit.init_flask()
    self.prep_controllers()

  def prep_controllers(self):
    self.manage_pw_controller: ManagerPwsController = ManagerPwsController()
    self.login_controller: LoginController = LoginController()

  def run(self):
    APIInit.flask.run()