import hashlib
import os
import base64
from Crypto import Random
from Crypto.Cipher import AES
from src.util.FileIO import FileIO
from src.sec.error.DbDecryptionError import DbDecryptionError

class AESCipher(object):

  def __init__(self, key):
    self.bs = AES.block_size
    self.key = hashlib.sha256(self.__b64EncodeKey(key)).digest()

  def __b64EncodeKey(self, key) -> bytes:
    return base64.b64encode(str.encode(key, 'utf-8'))

  def encrypt(self, raw):
    raw = self._pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode()))

  def decrypt(self, enc):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

  def _pad(self, s):
    return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

  def decrypt_db(self, dbPath: str):
    return self.decrypt(FileIO.get_bytes_from_file(dbPath))

  @staticmethod
  def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]

  @staticmethod
  def generate_key() -> bytes:
    return os.urandom(16)

  @staticmethod
  def get_decrypted_db(key: str, dbPath: str):
    try:
      cipher = AESCipher(key)
      return cipher.decrypt_db(dbPath)
    except Exception as _:
      raise DbDecryptionError()