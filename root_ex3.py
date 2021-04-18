def print_root(a, b, c):
    r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print('해는 {} 또는 {}입니다.'.format(r1, r1))

print_root(1, 4,-21)
print_root(1, -6, 8)

def get_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2

reuslt1, result2 = get_root(1, 2, -8)
print('해는', reuslt1, '또는', result2)