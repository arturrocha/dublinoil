import requests
from bs4 import BeautifulSoup

URL = 'https://www.cheapestoil.ie/heating-oil-prices/Dublin'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='MainContent_updPrices')

#print(soup)
#print(results)

#print('***************************************************')
#print('all elements start')
job_elems = results.find_all()
#print(job_elems)
#print('all elements end')
#print('***************************************************')

TABLE = {
    9: None,
    10: None,
    13: None,
}

# var.translate(TABLE)
#for thing in job_elems:
#    print('*********')
#    print('start')
#    try:
#        x = thing.encode()
#        #print(x)
#        print(x.decode('utf-8').translate(TABLE))
#        #print(thing.translate(TABLE))
#    except:
#        print('error')
#        print(thing)
#    print('end')
#    print('*********')


print('***************************************************')
print('start other')
x = str(soup.contents[3]).split('pricegridsupplier')
for thing in x:
    if 'MainContent_pnlOtherDistributors' in thing:
        print('exit')
        exit()
    print('sup start **')
    if 'href="../distributors/Dublin/' in thing:
        y = thing.split(' ')
        for z in y:
            if 'href' in z:
                print(z)
            if 'Price' in z:
                print(z)
    print('end **')
