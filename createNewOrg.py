import requests
import config
import csv
import urllib3

# This line handle the ssl certificate error. 
urllib3.disable_warnings()

# variables to get ids and authToken from the config file. 
ids = config.ids
authToken = config.authToken

# Read the csv file and iliterate each row to read the value. 
csvFile = config.csvFile



fileLocation = csvFile['fileLocation']
with open(fileLocation, 'r') as file:
    for row in file:
        rows = ''.join(row.split())
        # print(row)

# The headers used to pass Snyk ids and name of the new organization. 
        values = {'name': rows, 'groupId': ids['groupId'], 'sourceOrgId': ids['sourceOrgId']}
        
# The authentication headers used to authentication into Snyk. 
        headers = {
        'Content-Type': 'application/json',
        'Authorization': authToken['Authorization']
        }

# The variable for the URL. 
        url = 'https://api.snyk.io/v1/org'

# From here to print(response_body.text) is working code to make the request. 
        # print(url, values, headers)
        request = requests.post(url, json=values, headers=headers, verify=False)
        
        print(request.text)