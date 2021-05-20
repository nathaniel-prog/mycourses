import requests



my_url= requests.get('https://ipinfo.io/')



respond= my_url.json()

print(my_url.json())

print(respond['city'])

