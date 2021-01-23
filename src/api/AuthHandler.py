from src.api.SessionHandler import SessionHandler
from src.sec.JwtAuth import JwtAuth,JwtAuthMsg
from functools import wraps
from flask import request


class InternalAPIError(Exception):

  def __init__(self, message, returnCode, custom_header=None):
    self.msg = message
    self.rCode = returnCode
    self.custom_header = custom_header

    self.raise_error()

  def raise_error(self):
    return {"message": self.msg, "ok": False}, self.rCode, self.custom_header

def AuthenticationRequired():
  api_error = InternalAPIError(
    message=f"User must authenticate!",
    returnCode=401,
    custom_header={"WWW-Authenticate": "Digest realm=\"access to core app\""}
  )

  return api_error.raise_error()


class Authenticator:

  def __init__(self):
    pass

  @staticmethod
  def login(pw):
    pass
    # check PW here
    # if user is not None:
    #   jtoken = JwtAuth.encode_auth_token(custom_fields={"user_info": user.serialize()})
    #   SessionHandler.nsession(u=user.serialize(), token=jtoken)
    #   return jtoken
    # else:
    #   return None
  # Custom Auth Check Decorator, ensures they have a valid jwt token && session

