from functions import create_ike_policy, fmc_instance, create_host_object, create_net_object

if __name__ == "__main__":
    fmc = fmc_instance()
    create_net_object(fmc, "nettest", "1.1.1.0/24")
    create_host_object(fmc, "hosttest", "1.1.1.7")
    create_ike_policy(fmc, "test123", "AES-128","SHA",14)

    