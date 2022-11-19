from src.util.Logging import LogFactory
from flask import Flask, render_template, jsonify
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger
from src.persistence.DBManager import DBManager
from src.Config import Config

flask_ref: Flask = APIInit.flask

class SetupController:

  def __init__(self):
    LogFactory.MAIN_LOG.info('Start SetupController')

  @staticmethod
  @flask_ref.route('/is_fresh_install', methods=['GET'])
  @http_logger
  def check_db_init():
    db: DBManager = DBManager(Config.DB_PATH)
    if db.db_is_initialized():
        return {"status": "db_initialized"}, 409
    else:
        return {"status": "db_not_initialized"}, 200

  # TODO SETUP DB (takes in master key for setup)