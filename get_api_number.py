"""Get api

This script search through file for API number of defined type.
The file consists of lines: type_name API_number

This file can also be imported as a module and contains the following
functions:

    * get_api - returns API number of defined type
"""
def get_api(api_type):
    """Search through file for API number of defined type

    Parameters
    ----------
    type: str
        string which contains type of API number (e.g. weather)

    Returns
    -------
    str
        String which contains API number
    """
    with open('./api', 'r') as file:
        for line in file:
            if line.startswith(api_type):
                line = line.split()
                api = line[1]
        return api


if __name__ == '__main__':
    API_TYPE = 'test'
    assert get_api(API_TYPE) == "123456a"
