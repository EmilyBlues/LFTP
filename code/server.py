from LFTP import *

server = LFTP()
while True:
  print(server.rdp_recv())