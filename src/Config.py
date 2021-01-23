import json
import os

class Config:

  root_dir: str = f"{os.getcwd()}"

  conf_file_location: str = f"{root_dir}/conf.json"
  conf_file: dict
  LOG_DIR: str
  LOG_LEVEL: str

  DB_KEY_PATH: str
  MASTER_KEY_PATH: str

  DB_PATH: str

  ASSETS_DIR: str = f"{root_dir}/client"

  def __init__(self):
    pass

  @staticmethod
  def init_config():
    Config.conf_file = json.load(open(Config.conf_file_location))

    Config.LOG_DIR = Config.conf_file['logging']['log_dir']
    Config.LOG_LEVEL = Config.conf_file['logging']['log_level']

    Config.DB_KEY_PATH = Config.conf_file['keys']['db'] if 'keys' in Config.conf_file and 'db' in Config.conf_file['keys'] else ''
    Config.MASTER_KEY_PATH = Config.conf_file['keys']['master'] if 'keys' in Config.conf_file and 'master' in Config.conf_file['keys'] else ''
    Config.DB_PATH = Config.conf_file['db']['path'] if 'db' in Config.conf_file.keys() and 'path' in Config.conf_file['db'] else ''

  @staticmethod
  def update_config_file(newConf: dict):
    os.remove(Config.conf_file_location)
    json.dump(newConf, open(Config.conf_file_location,'w+'), indent=4)

    # re-initialize
    Config.init_config()

