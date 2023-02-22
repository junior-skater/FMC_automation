import fmcapi
from fmcapi.api_objects.object_services import *
from keys import *



def fmc_instance():
	 return fmcapi.fmc.FMC(host=host, username=username, password=password, autodeploy=False)

def create_net_object(fmc, name, value):
	net = fmcapi.Networks(fmc= fmc, name= name, value= value)		
	net.post()
	

def create_host_object(fmc, name, value):
	host = Hosts(fmc, name=name, value=value)
	host.post()

def create_ike_policy(fmc, name,encryption, hash, DH):
	'''ike_options = {
        "name": name,
        "encryption": encryption,
        "hash": hash,
        "diffieHellmanGroup": DH,
        "authenticationMethod": "Preshared Key",
        "lifetimeInSeconds": "86400"}'''
	ike = IKEv1Policies(fmc=fmc, name=name, encryption=encryption, hash=hash,diffieHellmanGroup=DH, authenticationMethod="Preshared Key", lifetimeInSeconds=86400)
	ike.post()
