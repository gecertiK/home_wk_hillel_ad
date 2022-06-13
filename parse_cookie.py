from urllib.parse import urlsplit, parse_qs


def parse_cookie(query: str) -> dict:
    url = query
    query = urlsplit(url).path
    replace_sign = query.replace(";", "&")
    params = parse_qs(replace_sign)
    return {k: v[0] for k, v in params.items()}


if __name__ == '__main__':
    print('Example:')
    print(parse_cookie('name=Dima#http://example.com/?$$$$$&&&&&&#####'))
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('name=David&sex=male&') == {'name': 'David', 'sex': 'male'}
    assert parse_cookie('name=DaviD') == {'name': 'DaviD'}
    assert parse_cookie('name=DAVID;pers=QueenOfPain&lvl=30') == {'name': 'DAVID', 'pers': 'QueenOfPain', 'lvl': '30'}
    assert parse_cookie('names=david/maria') == {'names': 'david/maria'}
    assert parse_cookie('') == {}
    assert parse_cookie('age=21;name=Dima&;pers=123123#name=david#') == {'age': '21', 'name': 'Dima', 'pers': '123123'}
    assert parse_cookie('pers=Invoker&atribut=Intelligence') == {'pers': 'Invoker', 'atribut': 'Intelligence'}
    assert parse_cookie('http://example.com/?$$$$$&&&&&&#####') == {}
    assert parse_cookie('name=Dima#http://example.com/?$$$$$&&&&&&#####') == {'name': 'Dima'}
    assert parse_cookie('name=D+A+V+I+D') == {'name': 'D A V I D'}
    print('Wow, you are doing pretty good. Time to check it!')
