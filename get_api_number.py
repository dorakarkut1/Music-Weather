"""Get api

This script search through file for API number of defined type.
The file consists of lines: type_name:API_number

This file can also be imported as a module and contains the following
functions:

    * get_api - returns API number of defined type
"""
def get_api(type):
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
	with open('./api', 'r') as f:
		for line in f:
			if line.startswith(type):
				line = line.split()
				api = line[1]
		return api


if __name__ == '__main__':
	type = 'weather'
	print(get_api(type))