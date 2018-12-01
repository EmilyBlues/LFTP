from LFTP import *

server = LFTP()
while True:
  server.rdp_recv()