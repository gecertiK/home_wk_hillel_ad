from urllib.parse import urlsplit, parse_qs
def parse(query: str) -> dict:
    url = query
    query = urlsplit(url).query
    params = parse_qs(query)
    return {k: v[0] for k, v in params.items()}

if __name__ == '__main__':
    print('Example:')
    print(parse('https://example.com/path/to/page?name=ferret&color=blue'))
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    print('Wow, you are doing pretty good. Time to check it!')
