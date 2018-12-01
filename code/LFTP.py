import socket

delimeter = '$'

class header():
  def __init__(self, seqNum = 0, ackNum = 0, rwnd = 0, checksum = 0, ACK = 0, SYN = 0, FIN = 0):
    self.seqNum = seqNum
    self.ackNum = ackNum
    self.ACK = ACK
    self.SYN = SYN
    self.FIN = FIN
    self.rwnd = rwnd
    self.checksum = checksum

  def to_string(self):
    return (str(self.seqNum) + delimeter + str(self.ackNum) + delimeter + 
      str(self.ACK) + delimeter + str(self.SYN) + delimeter + 
      str(self.FIN) + delimeter + str(self.rwnd) + delimeter + str(self.checksum))

class segment():
  def __init__(self, header, data):
    self.header = header
    self.data = data
  
  def to_string(self):
    return self.header.to_string() + delimeter + str(self.data)

class LFTP():
  def __init__(self):
    # initial data
    pass

  def rdp_send(self, data):
    pass

  def rdp_recv(self, filename):
    pass

  def connect(self):
    pass

  def listen(self):
    pass

  def accept(self):
    pass

  def __del__(self):
    # teardown
    pass