import scraperwiki
from pyquery import PyQuery
#import pyquery
import re

ROOT = 'https://fairemtl.ca'
dom = pyquery.PyQuery('%s/fr/projets' % ROOT)
pages = int(dom.find('.pager-last a').attr('href').split('%2C')[-1])

urls = []
for page in range(0, pages + 1):
    dom = pyquery.PyQuery('%s/fr/projets?page=0,%s' % (ROOT, page))
    urls.extend("%s%s" % (ROOT, a.attrib['href']) for a in dom.find('h3 a'))

for compteur, url in enumerate(urls):
    dom = pyquery.PyQuery(url)
    print("numero: %s" % (compteur + 1))
    print("url: %s" % url)
    print("projet: %s" % dom.find('h1').text())
    # description est parfois des <span>, parfois des <p>
    span = dom.find('.pane-node-body span')
    if span:
        description = span[-1].text
    else:
        p = dom.find('.pane-node-body p')
        description = " ".join([e.text for e in p])
    print("description: %s" % description)
    print("nombre_commentaires: %s" % re.findall(r'[0-9]+', dom.find('#tabs-0-footer li.last a')[0].text)[0])
    print("nombre_abonnes: %s" % dom.find('.js-subscribe_section_content span.count').text())
    print( "nombre_appuis: %s" % dom.find('.js-support_project span.count').text())
