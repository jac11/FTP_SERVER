#/usr/bin/env python 
import os
from threading import Thread
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class FTP_SERVER:

        def __init__(self):
      
             self.FTP_LOCAL()
        def FTP_LOCAL(self):
                authorizer = DummyAuthorizer()
                authorizer.add_user('user ','1234', '.', perm='elradfmwMT')
                authorizer.add_anonymous(os.getcwd())
                handler = FTPHandler
                handler.authorizer = authorizer
                address = ('', 21)
                server = FTPServer(address, handler)
                server.max_cons = 256
                server.max_cons_per_ip = 5
               
                server.serve_forever()
               
if __name__ == '__main__':
     FTP_SERVER()
     
     
     
