import requests 
import json 

headers = {
	'Accept': 'application/json',
	'Content-type': 'application/json',
	'Authorization' : 'Basic '
} 
url = 'https://<ip>'

response = requests.post(f'{url}/api/fmc_platform/v1/auth/generatetoken', headers=headers, verify=False)

print (response.content)