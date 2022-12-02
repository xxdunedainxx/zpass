from src.util.Logging import LogFactory
from flask import Flask, request, redirect
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger
from src.persistence.DBManager import DBManager
from src.util.networking.IP import IPHelpers
from src.Config import Config

flask_ref: Flask = APIInit.flask

class SetupController:

  def __init__(self):
    LogFactory.MAIN_LOG.info('Start SetupController')

  @staticmethod
  def __check_password_strength(pw) -> bool:
      return True

  @staticmethod
  def __check_setup_payload(payload: dict):
      if 'pw' not in payload.keys():
          return False
      else:
          return SetupController.__check_password_strength(payload['pw'])

  @staticmethod
  @flask_ref.route('/is_fresh_install', methods=['GET'])
  @http_logger
  def check_db_init():
    if DBManager.db_is_initialized(Config.DB_PATH):
        return {"status": "db_initialized"}, 409
    else:
        return {"status": "db_not_initialized"}, 200

  @staticmethod
  @flask_ref.route('/setup', methods=['POST'])
  @http_logger
  def setup():
    if DBManager.db_is_initialized(Config.DB_PATH):
        return {"status": "db_initialized"}, 409
    else:
        if SetupController.__check_setup_payload(request.get_json()) is False:
            return {"status" : "weak_password"}, 404
        else:
            db: DBManager = DBManager(Config.DB_PATH, key=request.get_json()['pw'])
            db.lazy_init_db()
            return {"status" : "db_created"}, 200
