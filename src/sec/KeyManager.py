from src.sec.Encryption import AESCipher
from src.util.Logging import LogFactory
from src.util.FileIO import FileIO
from src.Config import Config
from src.util.errors.ErrorFactory import errorStackTrace
from src.util.errors.GracefulErrorHandler import GracefulError
from src.util.RandomGenerator import RandomGenerator


class KeyManager:

  DB_KEY_LOCATION: str = ''
  MASTER_PW_KEY_LOCATION: str = ''

  def __init__(self):
    pass

  @staticmethod
  def check_db_key() -> bool:
    return Config.DB_KEY_PATH == '' or FileIO.file_exists(Config.DB_KEY_PATH) is False

  @staticmethod
  def check_master_key() -> bool:
    return Config.MASTER_KEY_PATH == '' or FileIO.file_exists(Config.MASTER_KEY_PATH) is False

  @staticmethod
  def check_keys():
    if KeyManager.check_db_key():
      LogFactory.MAIN_LOG.warning('DB KEY PATH IS NOT SET. MUST GENERATE DB KEY')
      KeyManager.generate_db_key()
    else:
      LogFactory.MAIN_LOG.info('DB Key exists :)')

    if KeyManager.check_master_key():
      LogFactory.MAIN_LOG.warning('MASTER KEY PATH IS NOT SET. MUST GENERATE MASTER KEY')
      KeyManager.generate_master_key()
    else:
      LogFactory.MAIN_LOG.info('Master key exists :)')

  @staticmethod
  def get_db_key() -> bytes:
    if KeyManager.check_db_key():
      LogFactory.MAIN_LOG.warning('DB KEY PATH IS NOT SET. MUST GENERATE DB KEY')
      KeyManager.generate_db_key()
    return FileIO.get_bytes_from_file(Config.DB_KEY_PATH)

  @staticmethod
  def get_master_key() -> bytes:
    if KeyManager.check_master_key():
      LogFactory.MAIN_LOG.warning('MASTER KEY PATH IS NOT SET. MUST GENERATE MASTER KEY')
      KeyManager.generate_master_key()
    return FileIO.get_bytes_from_file(Config.MASTER_KEY_PATH)

  @staticmethod
  def generate_db_key():
    try:
      LogFactory.MAIN_LOG.info('===== GENERATING DB KEY =====')
      key: bytes = AESCipher.generate_key()
      db_key_path = f"{Config.root_dir}/../{RandomGenerator.generate_random_string(10)}.zp"

      FileIO.generate_byte_file(db_key_path, key)
      FileIO.lock_down_file(db_key_path)

      nConf: dict = Config.conf_file
      nConf['keys'] = {} if 'keys' not in nConf.keys() else nConf['keys']
      nConf['keys']['db'] = db_key_path

      Config.update_config_file(nConf)

      LogFactory.MAIN_LOG.info('===== DB Key generated =====')
    except Exception as e:
      LogFactory.MAIN_LOG.error(f"Failed to generate db key with error: {errorStackTrace(e)}")
      GracefulError.handle_error('Failed to generate db key')

  @staticmethod
  def generate_master_key():
    try:
      LogFactory.MAIN_LOG.info('===== GENERATING MASTER KEY =====')
      key: bytes=AESCipher.generate_key()
      master_key_path = f"{Config.root_dir}/../{RandomGenerator.generate_random_string(10)}.zp"

      FileIO.generate_byte_file(master_key_path, key)
      FileIO.lock_down_file(master_key_path)

      nConf : dict = Config.conf_file
      nConf['keys'] = {} if 'keys' not in nConf.keys() else nConf['keys']
      nConf['keys']['master'] = master_key_path

      Config.update_config_file(nConf)

      LogFactory.MAIN_LOG.info('===== Master Key generated =====')
    except Exception as e:
      LogFactory.MAIN_LOG.error(f"Failed to generate master key with error: {errorStackTrace(e)}")
      GracefulError.handle_error('Failed to generate master key')
