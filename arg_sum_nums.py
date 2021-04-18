def sum_num(*args):
    print(len(args),'개의 인자',args)
    sum = 0
    for n in args:
        sum += n
    averge = sum / len(args)
    print('합계 :',sum, '평균 :',averge)


sum_num(10, 20, 30)
sum_num(10, 20, 30, 40, 50)


def min_nums(*args):
    print('최솟값은', min(args))

min_nums(10, 2, 9, 3)