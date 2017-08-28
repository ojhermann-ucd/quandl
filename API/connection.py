# imports
import json
import requests


def api_key(file_name):
	with open(file_name, "r") as source:
		return source.readline()

def get_time_series_data_json(api_file_name, database_code, dataset_code):
	return requests.get("https://www.quandl.com/api/v3/datasets/" + database_code + "/" + dataset_code + ".json?api_key=" + api_key("api_key.txt")).json()



if __name__ == "__main__":
	lme_cobolt = get_time_series_data_json("api_key.txt", "LME", "PR_CO")
	print(lme_cobolt['dataset'])