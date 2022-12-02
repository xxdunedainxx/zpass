from src.util.Logging import LogFactory
from flask import Flask, render_template, jsonify
from src.api.APIInit import APIInit
from src.api.decorators.HTTPLogger import http_logger

flask_ref: Flask = APIInit.flask

class MonitoringController:

  def __init__(self):
    LogFactory.MAIN_LOG.info('Start MonitoringController')

  @staticmethod
  @flask_ref.route('/ping', methods=['GET'])
  @http_logger
  def ping():
    LogFactory.MAIN_LOG.info("Got a ping")
    return "Im up", 200