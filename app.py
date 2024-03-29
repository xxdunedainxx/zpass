from src.AppInit import AppInit
from src.util.errors.ErrorFactory import errorStackTrace

if __name__ == '__main__':
  try:
    App: AppInit = AppInit()
    App.run()
    exit(0)
  except Exception as e:
    print(f"{errorStackTrace(e)}")
    exit(1)
