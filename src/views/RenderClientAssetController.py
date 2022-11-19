from src.Config import Config
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger
from src.util.networking.IP import IPHelpers
from src.util.FileIO import FileIO

from flask import Flask, request, send_from_directory
import os
flask_ref: Flask = APIInit.flask

class RenderClientAssetController:

  __setup_path: str = "html/setup.html"
  __ip_replace: str = "${MY_IP}"
  __my_ip: str = IPHelpers.my_ip()


  @staticmethod
  @flask_ref.route('/client/<path:path>')
  @http_logger
  def send_html(path):
      ROUTE_TO_METHOD_MAPPING: dict = {
          RenderClientAssetController.__setup_path: RenderClientAssetController.render_setup_page,
          "default" : RenderClientAssetController.default_render
      }

      if path in ROUTE_TO_METHOD_MAPPING.keys():
          return ROUTE_TO_METHOD_MAPPING[path]()
      else:
          return ROUTE_TO_METHOD_MAPPING["default"](path)

  @staticmethod
  def render_setup_page():
      rawFile: str = FileIO.read_file_content(f"{Config.ASSETS_DIR}{os.sep}{RenderClientAssetController.__setup_path}")
      rawFile = rawFile.replace(RenderClientAssetController.__ip_replace, RenderClientAssetController.__my_ip)
      return rawFile

  """
  Default Renderer for the html asset controller
  """
  @staticmethod
  def default_render(path):
      rawFile: str = f"{Config.ASSETS_DIR}{os.sep}"
      return send_from_directory(Config.ASSETS_DIR, path)