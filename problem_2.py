import requests
import datetime

apiURL = "https://data.lacity.org/resource/ngkp-kqkn.json"
query = "SELECT business_name, location_start_date ORDER BY location_start_date ASC LIMIT 1"
endpoint = '''{0}?$query={1}'''.format(apiURL, query)
request = requests.get(endpoint)
result = request.json()

businessName = result[0][u'business_name']
foundedDate = datetime.datetime.strptime(result[0][u'location_start_date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')

output = '''The oldest active business in Los Angeles is {0}, founded in {1}'''.format(
    businessName,
    foundedDate
)

print(output)
