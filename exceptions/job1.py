def calc_salt(num):
    try:
        return int(num) / 100
    except ValueError:
        print(f'invalid literal for int() with base 10: {num}')
        return 0.0


print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))