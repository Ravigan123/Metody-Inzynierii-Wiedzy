import random

def prostokatow(f, pp, kp, lp):
    dx = (kp - pp) / lp
    wynik = 0
    for x in range(lp):
        x = x * dx + pp
        f1 = eval(f)
        x += dx
        f2 = eval(f)
        wynik += 0.5 * dx * (f1 + f2)
    return wynik

funkcja = "3*x**3+5*x**2+3"
pocz_przedzialu = 0
kon_przedzialu = 1
lp = 100
calka = prostokatow(funkcja, pocz_przedzialu, kon_przedzialu, lp)
print(calka)


def monte_carlo(f, pp, kp, n):
    wynik = 0
    dx = kp - pp
    for i in range(n):
        wynik += f(pp+ random.uniform(0, dx))
    wynik *= dx / n
    return wynik

def funkcja(x):
    return 3*x**3+5*x**2+3
pocz_przedzialu = 0
kon_przedzialu = 1
n = 10000
calka = monte_carlo(funkcja, pocz_przedzialu, kon_przedzialu, n)
print(calka)