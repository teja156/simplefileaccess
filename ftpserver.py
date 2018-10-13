from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import SimpleHTTPServer
import SocketServer
import BaseHTTPServer
import os
import optparse
import threading

USERNAME = "user" #set your username by editing this value within the quotes
PASSWORD = "123456" #set your password by editing the value within the quotes

PATH = "/Users/tejaswaroop/Desktop" #Change this to the path to the directory on your computer which you want to make accessible by the server

SCRIPT_PATH = "/Users/tejaswaroop/Desktop/simplefileaccess" #Change this path to the location of the downloaded script folder on your computer
ANONYMOUS_PATH = SCRIPT_PATH+"/anonymous_ftp" 



uname=""
passwd=""

def initvars():
    uname=""
    passwd=""


print("PATH : ",PATH)

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):

        print("printing request : ",self.path)
        st = str(self.path)
      
        authorize(st,PATH,ANONYMOUS_PATH) #check if already authorized user, if not, then try to authorize now. If failed, then prohibit access
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def authorize(st,PATH,ANONYMOUS_PATH):
    li = list(st)
    global uname
    global passwd

    print("uname is ",uname)
    print("passwd is ",passwd)
    if(uname==USERNAME and passwd==PASSWORD):
        #This means, the user is already authorize so now provide access
        ind1 = li.index("/")
        add_path = st[ind1:]
        new_path = PATH+add_path
        print("Providing access to : ",new_path)

    else:
        #This means the user is not authorized
        #Try to authorize the user first
        if(("username=" in st) and ("passwd=" in st)):
            #This means the request contains the credentials
            ind1= li.index("=")
            ind2 = li.index("&")
            uname = st[ind1+1:ind2]
            print("Received username : ",uname)

            li = [li[i] for i in range(ind2,len(st))]
            ind1 = li.index("=")
            for i in range(ind1+1,len(li)):
                passwd= passwd+li[i]

            print("Received password : ",passwd)

            if(uname==USERNAME and passwd==PASSWORD):
                os.chdir(PATH)
            else:
                os.chdir(ANONYMOUS_PATH)
        else:
            #This means the user is not authorized and not even trying to get authorized, prohibit access
            print("Access prohibitted")
            os.chdir(SCRIPT_PATH)

            
def StartServer():
    print("Server is up")
    
    host = "127.0.0.1"
    port = 1560
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    handler = GetHandler
    os.chdir(SCRIPT_PATH)
        
    http_server = SocketServer.TCPServer((host,port),handler)        
    http_server.serve_forever()

print("Server starting")
initvars()

if __name__ == '__main__':
    cthread = threading.Thread(target=StartServer())
    cthread.daemon = True
    thread.start()

#StartServer()

