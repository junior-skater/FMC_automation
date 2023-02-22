from functions import SiteToSite
import csv 


def readcsv(csv):
    with open (csv, "r") as file:
        params = csv.DictReader(file)
    return params


def vpn_creation():
    vpn = SiteToSite()
    vpn.create_net_object("nettest", "1.1.1.0/24")
    vpn.create_host_object("hosttest", "1.1.1.7")
    vpn.create_ikev1_policy("test123", "AES-128","SHA",14)
    vpn.create_ikev2_policy("ikev2test","SHA","SHA","AES-256",14 )
    vpn.create_ikev1ipsec_proposal ("ikev1ipsec", "AES-256","SHA")
    vpn.create_ikev2ipsec_proposal("ikev2ipsec", "AES-256", "SHA-256")


if __name__ == "__main__":
    values = readcsv("file.csv")   
    vpn_creation(values)






    