import requests
import config
import csv
import urllib3

# This line handle the ssl certificate error. 
urllib3.disable_warnings()

# variables to get ids and authToken from the config file. 
ids = config.ids
authToken = config.authToken
restVersion = config.restAPIVersion

# The authentication headers used to authentication into Snyk. 
headers = {
'Authorization': authToken['Authorization']
}

# Parameters pass on the URL. 
parameters = {'version': restVersion['restVersion'], 'group_id': ids['groupId']}
# print(parameters)
# other
# The variable for the URL. 
# https://api.snyk.io/rest/orgs?version=2023-09-20&group_id={id}
url = 'https://api.snyk.io/rest/orgs'

# From here to print(response_body.text) is working code to make the request. 
# print(url, values, headers)
request = requests.get(url, params=parameters, headers=headers, verify=False)

size = len(request.json()['data'])
print(size)
print(type(request.json()['data']))


print(request.json()['data'][1]['attributes']['slug'])