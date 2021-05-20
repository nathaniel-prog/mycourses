import requests



my_url= requests.get('https://ipinfo.io/')

my_url2= requests.get(f'https://ipinfo.io/Jerusalem')

respond= my_url.json()

print(respond)

#print(my_url2.json())

print(respond['region'])


def come(*args , **kwargs):
	return args 

