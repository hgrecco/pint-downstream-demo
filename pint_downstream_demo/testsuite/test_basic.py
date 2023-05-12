import pint_downstream_demo as content


def test_basic():
    assert content.rotterdam < content.titanic
    assert content.titanic < content.wonder_of_the_seas
