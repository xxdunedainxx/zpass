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

from flask import Flask, request, send_from_directory
flask_ref: Flask = APIInit.flask


class RenderJS:

  @staticmethod
  @flask_ref.route('/js/<path:path>')
  @http_logger
  def send_js(path):
      return send_from_directory('js', path)