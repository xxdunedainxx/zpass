from src.Config import Config
from src.util.Logging import LogFactory
from src.util.RandomGenerator import RandomGenerator
from  src.sec.KeyManager import KeyManager
from src.sec.Encryption import AESCipher
from src.util.FileIO import FileIO

import json

class DBManager:

  def __init__(self, path: str):
    self.db_path = path
    self.db = self.load_db()

  def load_db(self):
    self.check_db_exists()
    cipher = AESCipher(key=KeyManager.get_db_key())
    db = json.loads(cipher.decrypt(FileIO.get_bytes_from_file(self.db_path)))
    return db

  def load(self,keys):
    pass

  def check_db_exists(self):
    if self.db_path == '' or FileIO.file_exists(self.db_path) is False:
      LogFactory.MAIN_LOG.warning('DB does not exist! Initializing!')
      self.db_path = f"{Config.root_dir}/../{RandomGenerator.generate_random_string(10)}.zp"

      nConf : dict = Config.conf_file
      nConf['db'] = {} if 'db' not in nConf.keys() else nConf['db']
      nConf['db']['path'] = self.db_path

      Config.update_config_file(nConf)

      self.db = {}
      self.db['masterpass'] = RandomGenerator.generate_random_string(10)

      LogFactory.MAIN_LOG.info(f"Your master password is {self.db['masterpass']}")

      self.write_db()

  def write_db(self):
    cipher = AESCipher(key=KeyManager.get_db_key())
    FileIO.generate_byte_file(
      path=Config.DB_PATH,
      bytes=cipher.encrypt(json.dumps(self.db))
    )

  # TODO tree structure
  def add_value(self, key, value):
    self.db[key] = value
    self.write_db()

  def fetch_value(self, key):
    return self.db[key] if key in self.db.keys() else ''