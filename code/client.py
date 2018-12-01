from LFTP import *

client = LFTP(type=1)
for data in ['Michael', 'Tracy', 'Sarah']:
  # 发送数据:
  client.rdp_send(data.encode())