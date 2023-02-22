import requests 
import json
from keys import token, url

headers = {
	'Accept': 'application/json',
	'Content-type': 'application/json',
	'x-auth-access-token' : token
}


#  create new network object in FMC
def create_net_object(name,value,type):
	data = {

		"name" : name,
        "value" : value,
        "overridable" : False,
        "description" : "new net object",
        "type": type

	}
	return requests.post(f'{url}/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks', headers=headers, json=data, verify=False)


#  create new ike policy
def create_ike_policy():
	pass 

#  create new ipsec policy
def create_ipsec_policy():
	pass 



	

 