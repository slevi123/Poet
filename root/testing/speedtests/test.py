from time import time


def measure_speed(func, name, *args, **kwargs):
    start = time()
    for _ in range(10000):
        func(*args, **kwargs)
    print(name, 'runned in: ', interval := time() - start)
    return interval


def szotagszam(sztring):
    return sum(
        map(sztring.lower().count, 'aáeéiíoóöőuúüű')
    )


def sztagszam(sztring):
    szam = 0
    for letter in sztring:
        if letter in 'aáeéiíoóöőuúüű':
            szam += 1
    return szam


measure_speed(szotagszam, 'mapsum', 'valami')
measure_speed(sztagszam, 'for', 'valami')
