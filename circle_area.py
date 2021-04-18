def circle_area_circum():
    radius = float(input('원의 반지름을 입력하세요 :'))
    area = radius**2* 3.14
    circum = radius *2 *3.14
    return area, circum

print(circle_area_circum())

