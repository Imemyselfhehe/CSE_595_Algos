try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
HTMLFile = open("html.txt", "r")
index = HTMLFile.read()
S = BeautifulSoup(index, 'lxml')
for tag in S.find_all('p'):
  print(f'{tag.name}: {tag.text}')
