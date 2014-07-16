from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

print ('enter = next article, y = open artcle, x = exit')
print ('-------------------------------------------')
while True:
    content = urlopen('http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=xml')
    xml = content.read()
    content.close()
    soup = BeautifulSoup(xml)
    links = soup.find_all('page')
    for l in links:
        choice = input('Would you like to read about ' + l.get('title') + '?')
        if choice == 'y':
            webbrowser.open_new_tab('http://en.wikipedia.org/wiki?curid='+l.get('id'))
        elif choice == 'x':
            exit(0)
