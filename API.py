import requests

api_url="http://api.openweathermap.org/data/2.5/weather"
city= input('City?')

params= {'q': city, 'appid': '792f34e72ac63903289d533ecd56bca2', 'units':'metric'}
res=requests.get(api_url, params=params)
#print (res.status_code)
#print (res.headers['Content-Type'])
data = res.json()
template ='Current temperature in {} is {}'
print (template. format( city, data ['main']['temp']))
