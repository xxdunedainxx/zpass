from src.util.Logging import LogFactory
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger
from src.util.networking.IP import IPHelpers
from src.Config import Config

from flask import Flask, request, send_from_directory
flask_ref: Flask = APIInit.flask


class RenderJS:

  @staticmethod
  @flask_ref.route('/js/<path:path>')
  @http_logger
  def send_js(path):
      return send_from_directory('js', path)

  @staticmethod
  def init_js_conf():
    LogFactory.MAIN_LOG.info('Init conf.js')
    with open(f"{Config.root_dir}/client/js/conf.js", 'w+') as jsconf:
      jsconf.write(f"var MYIP = \"{IPHelpers.my_ip()}\"")
