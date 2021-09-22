"""Get location

This script based on IP address gets and returns location of user.

This script requires that `socket and simple_geoip` be installed within the Python
environment you are running this script in. It also requires module get_api_number
from Music_Weather repository.

This file can also be imported as a module and contains the following
functions:

    * get_IP - returns IP address of user
    * get_location - calls get_IP and get_api functions and returns location of user
"""

import socket
from simple_geoip import GeoIP
from get_api_number import get_api

def get_IP() -> int:
    """Gets and returns IP address of user

    Parameters
    ----------
    None

    Returns
    -------
    int
        Int which contains IP address
    """

    host = socket.gethostname()
    port=0
    result = socket.getaddrinfo(host, port, socket.AF_INET6)
    return result[1][4][0]


def get_location() -> str:
    """Calls get_IP and get_api functions and returns location of user

    Parameters
    ----------
    None

    Returns
    -------
    str
        String which contains location
    """
    IP = get_IP()
    api = get_api("location")
    geoip = GeoIP(api)
    data = geoip.lookup(IP)
    return data['location']['city']



if __name__ == '__main__':
    get_location()
