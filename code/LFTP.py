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
  def __init__(self, port = 9000, type = 0):
    # initial data
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if type == 0:
      self.socket.bind(('127.0.0.1', port))
      print('Server run on 9000...')
    
  # data 必须是binary类型数据
  def rdp_send(self, data, addr = '127.0.0.1', port = 9000):
    self.socket.sendto(data, (addr, port))

  def rdp_recv(self):
    while True:
      # 接收数据:
      data = self.socket.recvfrom(1024)
      print('Received from %s:%s.' %data)

  def connect(self):
    pass

  def listen(self):
    pass

  def accept(self):
    pass

  def __del__(self):
    # teardown
    self.socket.close()
    pass