import urllib.request,json
from app.models import Quote

QUOTES_URL = None

def configure_request(app):
    """This function will get the value of url from the configurations

    Args:
        app ([type]): [description]
    """

    global QUOTES_URL
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    """This will get the quotes from the url
    """
    with urllib.request.urlopen(QUOTES_URL) as url:
        returned = url.read()
        response = json.loads(returned)
        
        return response

def process_quote(response):
    """This will process the results fro the quote search

    Args:
        response ([type]): [description]
    """
    if response:
        id = response['id']
        author = response['author']
        quote = response['quote']
    else:
        id = 1
        author = 'Ken Mbira'
        quote = 'This beat\'s the life'

    new_quote = Quote(id,author,quote)

    return new_quote