def print_root(a, b, c):
    r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print('해는 {}, 또는 {}입니다.'.format(r1, r2))

print_root(1, 2, -8)
print_root(2, -6, -8)