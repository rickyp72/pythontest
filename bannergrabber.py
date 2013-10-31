#!/usr/bin/env python
import socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
        
def checkVulns(banner):
     if ("FreeFloat Ftp Server (Version 1.00)" in banner):
         print "[+] FreeFloat FTP Server is vulnerable."
     elif ("/tnftpd/ " in banner):
         print "[+] tnftpd FTP Server is vulnerable."
     else:
         print "[-] FTP Server isn't vulnerable."       
     return 
        
# def main():
#     ip1 = '172.16.0.10'
#     ip2 = '192.168.142.2'
#     port = 21
    
def main():
  portList = [21,22,25,80,110,443]
  for x in range(1, 10):
      ip = '192.168.95.' + str(x)
      for port in portList:
          print "checking " + ip + ': ' + str(port)
          banner = retBanner(ip, port)
          if banner:
              print '[+] ' + ip + ': ' + banner
              checkVulns(banner)
if __name__ == '__main__':
  main()
    
#     banner1 = retBanner(ip1, port)
#     if banner1:
#         print '[+] ' + ip1 + ': ' + banner1.strip('\n')
#         checkVulns(banner1)
#     banner2 = retBanner(ip2, port)
#     if banner2:
#         print '[+] ' + ip2 + ': ' + banner2.strip('\n')
#         checkVulns(banner2)
# if __name__ == '__main__':
#     main()
        
    



# #    Error handling example
# try:
#     print "[+] 1337/0 = "+str(1337/0)
# except Exception, e:
#     print "[-] Error =  "+str(e)