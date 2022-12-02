from src.Config import Config
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger
from src.util.networking.IP import IPHelpers
from src.util.FileIO import FileIO

from flask import Flask, request, send_from_directory
import os
flask_ref: Flask = APIInit.flask

class RenderClientAssetController:

  # TODO also make port configurable
  __setup_path: str = "html/setup.html"
  __home_path: str = "html/home.html"
  __keys_path: str = "html/keys.html"
  __ip_replace: str = "${MY_IP}"
  __my_ip: str = IPHelpers.my_ip()


  @staticmethod
  @flask_ref.route('/client/<path:path>')
  @http_logger
  def send_html(path):
      ROUTE_TO_METHOD_MAPPING: dict = {
          RenderClientAssetController.__setup_path: RenderClientAssetController.render_setup_page,
          RenderClientAssetController.__home_path: RenderClientAssetController.render_home_page,
          RenderClientAssetController.__keys_path: RenderClientAssetController.render_keys_page,
          "default" : RenderClientAssetController.default_render
      }

      if path in ROUTE_TO_METHOD_MAPPING.keys():
          return ROUTE_TO_METHOD_MAPPING[path]()
      else:
          return ROUTE_TO_METHOD_MAPPING["default"](path)

  @staticmethod
  def render_setup_page():
      return RenderClientAssetController.__ip_replace_file(f"{Config.ASSETS_DIR}{os.sep}{RenderClientAssetController.__setup_path}")

  @staticmethod
  def render_home_page():
      return RenderClientAssetController.__ip_replace_file(f"{Config.ASSETS_DIR}{os.sep}{RenderClientAssetController.__home_path}")

  @staticmethod
  def render_keys_page():
      return RenderClientAssetController.__ip_replace_file(
          f"{Config.ASSETS_DIR}{os.sep}{RenderClientAssetController.__keys_path}")

  """
  Default Renderer for the html asset controller
  """
  @staticmethod
  def default_render(path):
      rawFile: str = f"{Config.ASSETS_DIR}{os.sep}"
      return send_from_directory(Config.ASSETS_DIR, path)

  """
  Executes a simple replace on an HTML file, replacing the IP placeholder with the host's IP
  """
  @staticmethod
  def __ip_replace_file(path: str) -> str:
      rawFile: str = FileIO.read_file_content(path)
      return rawFile.replace(RenderClientAssetController.__ip_replace, RenderClientAssetController.__my_ip)