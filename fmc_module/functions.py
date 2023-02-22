from fmcapi import *
# from fmcapi.api_objects.object_services import *
from keys import *



class SiteToSite():

	def __init__(self) -> None:
		pass

	# Create network objects
	def create_net_object(name, value):
		with FMC(host=host, username=username, password=password, autodeploy=False, 
		) as fmc:
			net = Networks(fmc=fmc, name= name, value= value)		
			net.post()
		
	#  Create hosts objects
	def create_host_object(name, value):
		with FMC(host=host, username=username, password=password, autodeploy=False, 
		) as fmc:

			myhost = Hosts(fmc=fmc, name=name, value=value)
			myhost.post()

	#  Create ike version 1 policy
	def create_ikev1_policy(name,encryption, hash, DH):
		with FMC(host=host, username=username, password=password, autodeploy=False, 
		) as fmc:
				ike = IKEv1Policies(fmc=fmc, name=name
				,encryption=encryption,
				hash=hash,diffieHellmanGroup=DH, 
				authenticationMethod="Preshared Key", 
				lifetimeInSeconds=86400,
				priority=20)
				ike.post()

	#  Create ike version 2 policy
	def create_ikev2_policy(name,
			integrityAlgorithms,
			prfIntegrityAlgorithms,
			encryptionAlgorithms,
			diffieHellmanGroups,):
		with FMC(host=host, username=username,
		password=password,autodeploy=False
		) as fmc:
			ike = IKEv2Policies(fmc=fmc, name= name,
				integrityAlgorithms= integrityAlgorithms,
				prfIntegrityAlgorithms= prfIntegrityAlgorithms,
				encryptionAlgorithms= encryptionAlgorithms,
				diffieHellmanGroups= diffieHellmanGroups)
			ike.post()

	#  Create ike version 1 IPSEC proposal
	def create_ikev1ipsec_proposal(name, espEncryption, espHash):
		with FMC(host=host, username=username,
		password=password,autodeploy=False
		) as fmc:
			ipsec = IKEv1IpsecProposals(fmc=fmc, name=name,
			espEncryption=espEncryption, espHash= espHash)
			ipsec.post()

	#  Create ike version 2 IPSEC proposal
	def create_ikev2ipsec_proposal(name, encryptionAlgorithms, integrityAlgorithms): 
		with FMC(host=host, username=username,
		password=password,autodeploy=False
		) as fmc:
			ipsec = IKEv2IpsecProposals(fmc=fmc, name=name,
				encryptionAlgorithms=encryptionAlgorithms,
				integrityAlgorithms=integrityAlgorithms)
			ipsec.post()

class SecPolicy():
	pass