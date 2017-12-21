import requests
malware = str(input("File Location\n"))

if malware == "r":
    headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
    params = {'apikey': 'd9dedb7ab5bfd4f4f4d7b3a43eee7606655eec73edbf793bd890bbbf4c21c2fa', 'resource':'http://www.virustotal.com'}
    response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',
    params=params, headers=headers)
    json_response = response.json()
    print(json_response["positives"])
else:
    params = {'apikey': 'd9dedb7ab5bfd4f4f4d7b3a43eee7606655eec73edbf793bd890bbbf4c21c2fa'}
    files = {'file': (malware, open(malware, 'rb'))}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
    json_response = response.json()
    print(json_response["verbose_msg"])
