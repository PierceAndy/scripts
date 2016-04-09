import os
import glob
import json


def main():

	pretty_directory = "./pretty_json"
	if not os.path.exists(pretty_directory):
		os.makedirs(pretty_directory)

	for json_file in glob.glob('*.json'):
		with open (json_file) as data:
			json_data = json.load(data)
			pretty_json_file = file(pretty_directory + '/' + json_file, 'w')
			json.dump(json_data, pretty_json_file, sort_keys=True, indent=4, separators=(',', ': '))
			pretty_json_file.close()


if __name__ == "__main__":
	main()
