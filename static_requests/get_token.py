import requests 
from keys import url

headers = {
	'Accept': 'application/json',
	'Content-type': 'application/json',
	'Authorization' : 'basic '
} 
data = {}

response = requests.post(f'{url}/api/fmc_platform/v1/auth/generatetoken', headers=headers, data=data, verify=False)
print(response.headers)