"""Get location

This script based on IP address gets and returns location of user.

This script requires that `re, json, urllib` are installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
function:

    * get_location - returns location of user
"""

import json
from urllib.request import urlopen


def get_location() -> str:
    """Returns location of user

    Parameters
    ----------
    None

    Returns
    -------
    str
        String which contains location (city name)
    """


    url = 'http://ipinfo.io/json'
    with urlopen(url) as response:
        data = json.load(response)
    return data['city']


if __name__ == '__main__':
    print(get_location())
