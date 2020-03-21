import fibgen


def pi_series():
    odds = fibgen.odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()
for x in range(100000):
    print(next(approx_pi))
