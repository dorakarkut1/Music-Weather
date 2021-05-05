
def get_api(type):
	with open('./api', 'r') as f:
		for line in f:
			if line.startswith(type):
				line = line.split()
				api = line[1]
		return api


if __name__ == '__main__':
	type = 'weather'
	get_api(type)