from dnac_config import get_device_list
from meraki_config import getOrganizationIDLists, getDeviceInfo

if __name__ == "__main__":
    # get_device_list()
    print(getDeviceInfo('L_566327653141856846', 'Q2KD-KWMU-7U92'))