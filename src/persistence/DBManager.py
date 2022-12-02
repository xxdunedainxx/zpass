import os

from src.Config import Config
from src.util.Logging import LogFactory
from src.util.RandomGenerator import RandomGenerator
from src.sec.Encryption import AESCipher
from src.util.FileIO import FileIO

import json

class DBManager:

  def __init__(self, path: str, key: str):
    self.cipher = AESCipher(key=key)
    self.db_path = path
    self.db = self.load_db(key)

  def load_db(self, key: str):
    self.lazy_init_db()
    db = json.loads(self.cipher.decrypt(FileIO.get_bytes_from_file(self.db_path)))
    return db

  def load(self,keys):
    pass

  @staticmethod
  def db_is_initialized(dbPath: str):
    return FileIO.file_exists(dbPath) is True

  def lazy_init_db(self):
    if DBManager.db_is_initialized(self.db_path) is False:
      LogFactory.MAIN_LOG.warning('DB does not exist! Initializing!')
      self.db_path = f"{Config.root_dir}{os.sep}..{os.sep}{RandomGenerator.generate_random_string(10)}.zp"

      nConf : dict = Config.conf_file
      nConf['db'] = {} if 'db' not in nConf.keys() else nConf['db']
      nConf['db']['path'] = self.db_path

      Config.update_config_file(nConf)

      self.db = {}

      self.write_db()

  def write_db(self):
    FileIO.generate_byte_file(
      path=Config.DB_PATH,
      bytes=self.cipher.encrypt(json.dumps(self.db))
    )

  # TODO tree structure
  def add_value(self, key, value):
    self.db[key] = value
    self.write_db()

  def fetch_value(self, key):
    return self.db[key] if key in self.db.keys() else ''