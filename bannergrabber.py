#!/usr/bin/env python
import socket
import os
import sys
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
        
def checkVulns(banner, filename):
    f = open(filename,'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is vulnerable: "+banner.strip('\n')   

    
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print 'checking file exists'
        if not os.path.isfile(filename):
            print '[-] ' + filename + ' does not exist.'
            exit(0)
        print "File exits\n"
        print 'checking access'
        if not os.access(filename, os.R_OK):
            print '[-] ' + filename + ' access denied.'
            exit(0)
        print "Access good\n"
    else:
        print '[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>'
        exit(0)
    portList = [21,22,25,80,110,443]
    for x in range(8, 11):
        ip = '172.16.0.' + str(x)
        for port in portList:
            print "checking " + ip + ': ' + str(port)
            banner = retBanner(ip, port)
            if banner:
                print '[+] ' + ip + ': ' + banner
                checkVulns(banner, filename)
if __name__ == '__main__':
    main()
    
