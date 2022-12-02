from src.util.Logging import LogFactory
from src.Config import Config
from src.sec.KeyManager import KeyManager
from src.persistence.DBManager import DBManager
from src.api.APIFactory import APIFactory
from src.sec.JwtAuth import JwtAuth

class AppInit:

  def __init__(self):
    self.utility_init()

  def utility_init(self):
    Config.init_config()
    LogFactory.log_dir = Config.LOG_DIR
    LogFactory.log_level = Config.LOG_LEVEL
    LogFactory.main_log()

  def run(self):
    LogFactory.MAIN_LOG.info('===== START RUNNING APPLICATION =====')

    api: APIFactory = APIFactory()
    api.run()

