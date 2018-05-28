from algorithm import gcd


def test_gcd():
    assert 200 == gcd.gcd(1000, 200)
    assert 200 == gcd.gcd_stein(1000, 200)
    assert 200 == gcd.gcd(200, 1000)
    assert 200 == gcd.gcd_stein(200, 1000)
    assert 21 == gcd.gcd(1071, 462)
    assert 21 == gcd.gcd_stein(1071, 462)
