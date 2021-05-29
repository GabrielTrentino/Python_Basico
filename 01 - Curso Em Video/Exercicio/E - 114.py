import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print('O site Pudim está indisponivel no momento.')
else:
    print('Tudo ok')