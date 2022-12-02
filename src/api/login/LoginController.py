from src.util.Logging import LogFactory
from src.Config import Config
from flask import Flask, render_template, jsonify
from src.api.APIInit import APIInit
from src.sec.Encryption import AESCipher
from src.sec.error.DbDecryptionError import DbDecryptionError
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
    try:
      AESCipher.get_decrypted_db(key=data['pw'], dbPath=Config.DB_PATH)
      return jsonify({'message': 'authorized', 'jwt': JwtAuth.encode_auth_token(custom_fields={'pw': data['pw']})})
    except DbDecryptionError as dbEncryptError:
      return jsonify({'message': 'unauthorized'}), 401
    except Exception as e:
      return jsonify({'message': 'internal server error'}), 500