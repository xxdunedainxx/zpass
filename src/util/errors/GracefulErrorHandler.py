from src.util.Logging import LogFactory

class GracefulError:

  def __init__(self):
    pass

  @staticmethod
  def handle_error(error: str = ''):
    try:
      LogFactory.MAIN_LOG.error(f"Trying to shutdown with fatal error {error}")
      exit(-1)
    except Exception as e:
      print(e)