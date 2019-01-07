import query_any_url as qnu

X_URL = 'http://www.example.com/'
obj = qnu.QueryApi()


def test_valid_syntax():
    result = obj.is_valid_syntax(X_URL)
    assert result


def test_save_url():
    obj.save_url(X_URL)
    assert X_URL in obj.urls.values()


def test_get_status():
    assert obj.get_status(X_URL) == 200


def test_check_status():
    assert obj.check_status(X_URL)
