from urllib.parse import urlsplit, parse_qs


def parse(query: str) -> dict:
    url = query
    query = urlsplit(url).query
    params = parse_qs(query)
    return {k: v[0] for k, v in params.items()}


if __name__ == '__main__':
    print('Example:')
    print(parse('http://example.com/?name=D+A+V+I+D'))
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('http://example.com/?name=David&sex=male&') == {'name': 'David', 'sex': 'male'}
    assert parse('http://example.com/?name=DaviD') == {'name': 'DaviD'}
    assert parse('http://example.com?name=DAVID&pers=QueenOfPain&lvl=30') == {'name': 'DAVID', 'pers': 'QueenOfPain', 'lvl': '30'}
    assert parse('http://example.com/?names=david/maria') == {'names': 'david/maria'}
    assert parse('') == {}
    assert parse('http://example.com/???name=Dima&&&&&&&&pers=123123#name=david') == {'name': 'Dima', 'pers': '123123'}
    assert parse('http://example.com/?pers=Invoker&atribut=Intelligence') == {'pers': 'Invoker', 'atribut': 'Intelligence'}
    assert parse('http://example.com/?$$$$$&&&&&&#####') == {}
    assert parse('http://example.com/?name=Dima$#$#$#$#$#$#$') == {'name': 'Dima$'}
    assert parse('http://example.com/?name=D+A+V+I+D') == {'name': 'D A V I D'}
    print('Wow, you are doing pretty good. Time to check it!')
