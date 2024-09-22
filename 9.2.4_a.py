import requests

flag = requests.get('http://python-sandbox:8080/all/together/exercise1')
print(flag.text)
