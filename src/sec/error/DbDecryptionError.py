class DbDecryptionError(Exception):
  def __init__(self):
    super().__init__("DB Decryption failed..")