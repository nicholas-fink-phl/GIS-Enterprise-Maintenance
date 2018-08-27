# import python modules needed to run script
import requests
import json
import unicodecsv
from datetime import datetime

# get the start time for the script
start = datetime.now()

# creates a reusable session to speed up api calls
session = requests.session()

# api url
api_url = 'https://www.opendataphilly.org/api/3/action/organization_show?id=city-of-philadelphia&include_datasets=true&include_extras=false&include_users=false&inlcude_groups=false&include_tags=false&include_followers=false'

# setup the request to the api
r = session.get(api_url, stream=True)
raw = r.text
data = json.loads(r.content)
datas = data['result']['packages']

# headers identify application type for the server
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

# create an empty list to store data later
li = []

for i in datas:
    # get the info for every dataset in open data philly
    for x in i['resources']:
        url = x['url']
        slug = i['name']
        title = i['title']
        name = x['name']
        frmt = x['format']
        http = url.replace('https', 'http')

        print(url)

        try:
            # test out the url and return the status code and append the info to the list
            test = session.get(url, headers=headers, stream=True)
            print(test.status_code)
            li.append([name, title, slug, frmt, test.status_code, url, ''])
        except Exception as e:
            # if there's an error, log the error, note that a status couldn't be returned, and continue the loop
            li.append([name, title, slug, frmt, 'No status code', url, e])
            continue

# create a csv file to write the list to
file = r'odp_endpoints_check.csv'
f = open(file, 'wb')
writer = unicodecsv.writer(f)
writer.writerows(li)

# get the total run time
end = datetime.now()
total = end - start
print('Finished in '+str(total)+' hours.')
