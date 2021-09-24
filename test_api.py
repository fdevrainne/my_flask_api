import requests

from constant import BASE_URL, END_POINT

method = "common"
column = "MiscFeature"

url = "/".join([BASE_URL, END_POINT])
params = {"method":method, "column":column}
response = requests.get(url, params=params)

print(f"- The call tested is a get request to the following url: \n  {url} \n  with the following parameters: {params}\n")
print(f"- The status code of the API for the call is: {response.status_code} \n  with the following result: {response.json()}")


