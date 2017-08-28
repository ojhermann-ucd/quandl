# imports
import requests


def api_key(file_name):
	with open(file_name, "r") as source:
		return source.readline()

def get_time_series_data_json(api_file_name, database_code, dataset_code):
	url = "https://www.quandl.com/api/v3/datasets/"
	payload = {database_code:"/", dataset_code:"/", "data.json?api_key=":api_key(api_file_name)}
	r = requests.get(url, params=payload)
	return r.json()

print(get_time_series_data_json("api_key.txt", "WIKI", "FB"))