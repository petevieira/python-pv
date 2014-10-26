import urllib
import re

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    m = re.search('id="ref_(.*?)">(.*?)<', content)
    if m:
        quote = m.group(2)
    else:
        quote = 'no quote available for: ' + symbol
    return quote
