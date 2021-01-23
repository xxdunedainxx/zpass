from src.util.Logging import LogFactory
from src.Config import Config
from src.sec.KeyManager import KeyManager
from src.persistence.DBManager import DBManager
from flask import Flask, render_template, jsonify
from src.api.APIInit import APIInit
from src.api.AuthHandler import Authenticator
from src.api.decorators.HTTPLogger import http_logger
from src.sec.JwtAuth import JwtAuth

from flask import request

flask_ref: Flask = APIInit.flask

class LoginController:

  def __init__(self):
    LogFactory.MAIN_LOG.info('Start LoginController')

  @staticmethod
  @flask_ref.route('/login', methods=['POST'])
  @http_logger
  def login():
    LogFactory.MAIN_LOG.info("Attempting login")
    data = request.get_json()
    db: DBManager = DBManager(Config.DB_PATH)

    if 'pw' in data.keys() and data['pw'] == db.db['masterpass']:
      return jsonify({'message' : 'authorized','jwt' : JwtAuth.encode_auth_token()})
    else:
      return jsonify({'message': 'unauthorized'}), 401