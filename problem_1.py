import requests

apiURL = "https://data.lacity.org/resource/ngkp-kqkn.json"
query = "SELECT COUNT(business_name), business_name GROUP BY business_name ORDER BY COUNT_business_name DESC LIMIT 1"
endpoint = '''{0}?$query={1}'''.format(apiURL, query)
request = requests.get(endpoint)
result = request.json()

output = '''The business with the most locations in Los Angeles is {0}, with {1} locations'''.format(
    result[0][u'business_name'],
    result[0][u'COUNT_business_name'],
)

print(output)
