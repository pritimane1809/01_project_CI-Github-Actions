import app

def test_add():
    assert app.add(3, 4) == 7
    assert app.add(-1, 1) == 0
