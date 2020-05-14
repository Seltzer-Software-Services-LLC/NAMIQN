import requests

url = "https://api.walkertracker.com/api/2.1/admin_competition_data/55966"

payload = {'token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}
files = [

]
headers = {
  'Cookie': 'PROXYSESSID=https://10.100.101.95:443'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
