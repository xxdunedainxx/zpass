from src.util.Logging import LogFactory
from src.Config import Config
from src.sec.KeyManager import KeyManager
from src.persistence.DBManager import DBManager
from flask import Flask, render_template, jsonify
from src.api.APIInit import APIInit
from src.api.AuthHandler import Authenticator
from src.api.decorators.HTTPLogger import http_logger
from src.api.decorators.Authenticate import httpauthenticate
from src.util.errors.ErrorFactory import errorStackTrace, InternalAPIError

from flask import request

flask_ref: Flask = APIInit.flask

class ManagerPwsController:

  def __init__(self):
    LogFactory.MAIN_LOG.info('Start ManagePwsController')

  @staticmethod
  @flask_ref.route('/get_pws', methods=['GET'])
  @http_logger
  @httpauthenticate
  def get_pws():
    try:
      LogFactory.MAIN_LOG.info("Fetching pws")
      db: DBManager = DBManager(Config.DB_PATH)
      return jsonify(db.db)
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
        db: DBManager = DBManager(Config.DB_PATH)
        db.add_value(data['key'], data['value'])
        return {'message' : 'yay'}
      else:
        return {'message': 'key and value required for this api'}
    except Exception as e:
      LogFactory.MAIN_LOG.error(f"Failed fetching db {errorStackTrace(e)}")
      raise InternalAPIError('Something went wrong :(', 500)