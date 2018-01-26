#!/usr/bin/python
#coding: utf-8
#Code By : Gad
import requests
gad ="[+]Facebook Rating By Token[+]\n[+]Coded: @Gad990   (Telegram)[+]\n Date: 26/01/2018 \n[+]Changing the Description of this tool Won't made you the coder ^_^[+]\n[+]I take no responsibilities for the use of this program[+] "
print(gad)
id_page = input('Enter ID >>')
rat = input('Enter Ratting >>')
token = input('Enter token Folder >>')
var = open(token, 'r').readlines()
for line in var:
	token = line.strip()
	url = '	https://graph.facebook.com/'+id_page+'/ratings?Name=goodpagegoodpostsgoodadminsgoodpagegoodpostsgoodadmins&rating='+rat+'&access_token='+token+'&method=post'
	http = requests.post(url)
	content = http.content
	print(content)
