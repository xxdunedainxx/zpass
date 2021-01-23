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

    #JwtAuth.set_jwt_algorithm()

  def __check_db(self):
    db: DBManager = DBManager(Config.DB_PATH)
    db.check_db_exists()

  def run(self):
    LogFactory.MAIN_LOG.info('===== START RUNNING APPLICATION =====')
    KeyManager.check_keys()
    self.__check_db()

    api: APIFactory = APIFactory()
    api.run()

