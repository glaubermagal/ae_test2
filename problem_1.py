import requests
r = requests.get('https://data.lacity.org/resource/ngkp-kqkn.json?$query=SELECT COUNT(business_name), business_name GROUP BY business_name ORDER BY COUNT_business_name DESC LIMIT 1')
print(r.json())