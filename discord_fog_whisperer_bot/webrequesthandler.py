import requests

def verify_wiki_link(link):
    response = requests.get('https://deadbydaylight.fandom.com/')
    return response.status_code < 400