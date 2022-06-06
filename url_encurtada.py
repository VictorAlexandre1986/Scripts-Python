import pyshorteners

url='https://www.terra.com.br'

s = pyshorteners.Shortener()

shortURL = s.tinyurl.short(url)

print(f'URL encurtada : {shortURL}')