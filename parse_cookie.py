from urllib.parse import urlsplit, parse_qs
def parse_cookie(query: str) -> dict:
    url = query
    query = urlsplit(url).path
    replace_sign = query.replace(";", "&")
    params = parse_qs(replace_sign)
    return {k: v[0] for k, v in params.items()}


if __name__ == '__main__':
    print('Example:')
    print(parse_cookie('name=Dima;age=28;'))
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('name=Axe;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Maria;age=21;') == {'name': 'Maria', 'age': '21'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('"''"') == {}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    print('Wow, you are doing pretty good. Time to check it!')