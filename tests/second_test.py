from uvdatabricks.utils.op import suma


def test_suma():
    result = suma(2, 3)
    assert result == 5
