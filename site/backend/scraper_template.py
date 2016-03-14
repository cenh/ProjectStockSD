from lxml import html
from urllib import parse as urlparse
import sys

def main():
    ansatte_url = 'http://diku.dk/Ansatte'

    tree = html.parse(ansatte_url)

    def make_links_absolute(soup, url):
        for tag in soup.iter('a'):
            if 'href' in tag.attrib:
                tag.attrib['href'] = urlparse.urljoin(url, tag.attrib['href'])

    make_links_absolute(tree, ansatte_url)

    # Medarbejdertable
    table = tree.find('table')#tree.xpath("//table[@id='medarbejdertable']")[0]

    for row in tree.iter('tr'):
        for column in row.iter('td'):
            for link in column.iter('a'):
                print('Name: ' + link.text)
                print('Link: ' + link.attrib['href'])
                #employee = html.parse(link.attrib['href'])
            print(column.text)

#<td valign='top'><a href="LINK">NAVN</a></td><td valign='top'>STILLING</td><td valign='top'>ARBEJDSOMRÅDE</td><td valign='top'>TELEFON</td><td valign='top'>EMAIL</td>

if __name__ == "__main__":
    main()
