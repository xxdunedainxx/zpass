from src.util.Logging import LogFactory
from src.Config import Config

from flask import Flask, render_template, jsonify
from flask_cors import CORS

class APIInit:

  flask: Flask = Flask(__name__)

  def __init__(self):
    pass

  @staticmethod
  def init_flask():
    LogFactory.MAIN_LOG.info('Start flask API')
    CORS(APIInit.flask)
