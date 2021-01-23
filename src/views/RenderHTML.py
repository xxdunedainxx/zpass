from src.Config import Config
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger

from flask import Flask, request, send_from_directory
flask_ref: Flask = APIInit.flask

class RenderHTML:

  @staticmethod
  @flask_ref.route('/client/<path:path>')
  @http_logger
  def send_html(path):
      return send_from_directory(Config.ASSETS_DIR, path)