class InternalAPIError(Exception):

  def __init__(self, message, returnCode, custom_header=None):
    self.msg = message
    self.rCode = returnCode
    self.custom_header = custom_header

    self.raise_error()

  def raise_error(self):
    return {"message": self.msg, "ok": False}, self.rCode, self.custom_header