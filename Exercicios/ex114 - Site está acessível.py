"""
Crie um código em Python que teste se um site está acessível pelo computador utilizado.
"""

import urllib
import urllib.request

url = 'http://www.google.com.br'

try:
    site = urllib.request.urlopen(url)
except:
    print(f'Não foi possível acessar a URL "{url}".')
else:
    print(f'O site "{url}" está acessível pelo seu computador.')
    print(site.read())