import requests
import config
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

# The variable for the URL. 
# https://api.snyk.io/rest/orgs?version=2023-09-20&group_id={id}
url = 'https://api.snyk.io/rest/orgs'

# From here to print(response_body.text) is working code to make the request. 
# print(url, values, headers)
request = requests.get(url, params=parameters, headers=headers, verify=False)

def write_to_csv():
    with open('nameSlug.csv','w') as file:
        data = request.json()
        items = data['data']
        for item in items:
            name = item['attributes']['name']
            slug = item['attributes']['slug']
            file.write(name + ',' + slug)
            file.write('\n')
  

write_to_csv()



