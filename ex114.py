import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro no Pudim')
else:
    print('Tudo ok no Pudim')
    print(site.read())# dá o conteúdo html do site

#testa se o site está no ar
#com wifi desligado diz que deu erro