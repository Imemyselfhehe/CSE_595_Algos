import sys
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
HTMLFile = open(sys.argv[1], "r")
index = HTMLFile.read()
S = BeautifulSoup(index, 'lxml')
for tag in S.find_all(sys.argv[2]):
  print(f'{tag.name}: {tag.text}')
