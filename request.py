import requests
import re
 
username = "natas0"
password = username
url = 'http://%s.natas.labs.overthewire.org', username
respone = requests.get(url, auth=(username,password))
content= respone.text
print(re.findall('<!--The password for natas1 is (.*) -->',content))