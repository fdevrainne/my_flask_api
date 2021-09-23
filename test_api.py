import requests

from constant import BASE_URL, END_POINT

method = "common"
column = "MiscFeature"

url = "/".join([BASE_URL, END_POINT, method, column])
response = requests.get(url)

print(f"- The call tested is a get request to the following url: \n  {url}\n")
print(f"- The status code of the API for the call is: {response.status_code} \n  with the following result: {response.json()}")


