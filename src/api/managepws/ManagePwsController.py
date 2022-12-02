from src.util.Logging import LogFactory
from src.Config import Config
from src.persistence.DBManager import DBManager
from flask import Flask, jsonify
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger
from src.api.decorators.Authenticate import httpauthenticate
from src.util.errors.ErrorFactory import errorStackTrace, InternalAPIError
from src.sec.JwtAuth import JwtAuth

from flask import request

flask_ref: Flask = APIInit.flask

class ManagerPwsController:

  def __init__(self):
    LogFactory.MAIN_LOG.info('Start ManagePwsController')

  @staticmethod
  def __get_pw_from_jwt() -> str:
    return JwtAuth.get_pw_from_auth_token(request.headers.get('X-Authentication'))

  @staticmethod
  @flask_ref.route('/get_pws', methods=['GET'])
  @http_logger
  @httpauthenticate
  def get_pws():
    try:
      LogFactory.MAIN_LOG.info("Fetching pws")
      db: DBManager = DBManager(Config.DB_PATH, ManagerPwsController.__get_pw_from_jwt())
      return jsonify(db.db)
    except Exception as e:
      LogFactory.MAIN_LOG.error(f"Failed fetching db {errorStackTrace(e)}")
      raise InternalAPIError('Something went wrong :(', 500)

  @staticmethod
  @flask_ref.route('/dump_keys', methods=['POST'])
  @http_logger
  @httpauthenticate
  def dump_keys():
    try:
      LogFactory.MAIN_LOG.info('processing update request')
      data=request.get_json()
      db: DBManager = DBManager(Config.DB_PATH, ManagerPwsController.__get_pw_from_jwt())
      db.db = data
      db.write_db()
      return {'message' : 'db updated'}
    except Exception as e:
      LogFactory.MAIN_LOG.error(f"Failed fetching db {errorStackTrace(e)}")
      raise InternalAPIError('Something went wrong :(', 500)

  @staticmethod
  @flask_ref.route('/update_pws', methods=['POST'])
  @http_logger
  @httpauthenticate
  def update_pw():
    try:
      LogFactory.MAIN_LOG.info('processing update request')
      data=request.get_json()
      if 'key' in data.keys() and 'value' in data.keys():
        db: DBManager = DBManager(Config.DB_PATH, ManagerPwsController.__get_pw_from_jwt())
        db.add_value(data['key'], data['value'])
        return {'message' : 'yay'}
      else:
        return {'message': 'key and value required for this api'}
    except Exception as e:
      LogFactory.MAIN_LOG.error(f"Failed fetching db {errorStackTrace(e)}")
      raise InternalAPIError('Something went wrong :(', 500)