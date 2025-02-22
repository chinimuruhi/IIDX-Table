import requests

filePath = './dist/test.json'
url = 'https://sp12.iidx.app/api/v1/sheets'

with open(filePath, mode='w') as f:
    r = requests.get(url)
    f.write(r.text)