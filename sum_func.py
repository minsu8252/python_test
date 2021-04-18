def print_sub(a, b):
    result = a - b
    print(a,'과 ',b,'의 차는 ',result,'입니다.')

print_sub(10, 20)

def print_sub2(a, b):
    result = a - b
    print('{}과 {}의 차는 {}입니다.'.format(a,b,result))
print_sub2(2, 1)