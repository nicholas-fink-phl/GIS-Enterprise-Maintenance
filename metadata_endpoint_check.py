# import python modules needed to run script
import requests
import json
import unicodecsv
from datetime import datetime

# get the start time for the script
start = datetime.now()

# knack application id info
app_id = '' # alphanumeric string
api_key = '' # alphanumeric string
auth = {
    "X-Knack-Application-Id": app_id,
    "X-Knack-REST-API-Key": api_key
    }

# creates a reusable session to speed up api calls
session = requests.session()

# api url
api_url = 'https://api.knackhq.com/v1/objects/object_4/records/export?type=json'

# setup the request to the api
r = requests.get(api_url, headers=auth, stream=True)
raw = r.text
data = json.loads(r.content)
datas = data['records']

# headers identify application type for the server
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

# create an empty list to store data later
li = []

for i in datas:
    # get the url, format, and repository for every record in the knack representations table
    url = i['field_25_raw']['url']
    frmt = i['field_12_raw']
    repo = i['field_15_raw']

    print(url)

    try:
        # test out the url and return the status code and append the info to the list
        test = session.get(url, headers=headers, stream=True)
        print(test.status_code)
        li.append([str(i['field_13_raw'][0]['identifier']), str(frmt), str(repo), str(test.status_code), str(url), ''])
    except Exception as e:
        # if there's an error, log the error, note that a status couldn't be returned, and continue the loop
        if i['field_13_raw']:
            li.append([i['field_13_raw'][0]['identifier'], str(frmt), str(repo), 'No status code', str(url), str(e)])
        else:
            li.append(['', str(frmt), str(repo), 'No status code', str(url), str(e)])
        continue

# create a csv file to write the list to
file = r'metadata_endpoints_check.csv'
f = open(file, 'wb')
writer = unicodecsv.writer(f)
writer.writerows(li)

# get the total run time
end = datetime.now()
total = end - start
print('Finished in '+str(total)+' hours.')
