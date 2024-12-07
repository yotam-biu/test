 from hello import read_hello

def test_hello():
    assert read_hello('hello_.txt').strip() == '"hello"'
