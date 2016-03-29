#!/usr/bin/env python

from splinter import Browser
from bs4 import BeautifulSoup
from time import sleep
import sys

separator = ''.join( [ '-' * 175 ] )

if( len( sys.argv ) > 1 ):
        query = sys.argv[1]
else:
        exit( 'No query specified' )

print( 'Searching...\n%s' % separator )
with Browser( 'phantomjs' ) as browser:
        browser.visit('https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=' + query )
        sleep(1)
        #print( browser.html )
        soup = BeautifulSoup( browser.html, 'html.parser' )

links = soup.find_all( 'div', class_ = 'g' )
i = 1
for link in links:
        try:
                if( len( sys.argv ) > 2 and sys.argv[2] == '--links' ):
                        print( "%s -> %s\n\tsource -> %s\n\tlink -> %s\n%s"
                                % ( i, ' '.join ( link.find( 'span', class_ = 'st').text.split() ),
                                        link.find( 'cite' ).text, link.h3.a['href'].split('q=')[1], separator ) )
                else:
                        print( "%s -> %s\n\tsource -> %s\n%s"
                                % ( i, ' '.join ( link.find( 'span', class_ = 'st').text.split() ),
                                        link.find( 'cite' ).text, separator ) )
                i += 1
        except Exception:
                pass
