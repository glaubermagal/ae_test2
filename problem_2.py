import requests
r = requests.get('https://data.lacity.org/resource/ngkp-kqkn.json?$query=SELECT business_name,location_start_date ORDER BY location_start_date ASC LIMIT 1')
print(r.json())