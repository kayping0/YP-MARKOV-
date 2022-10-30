def area(figure, data):
    if figure == 'круг':
        print(data[0])
        res = 3.14*(data[0]**2)
    if figure == 'квадрат':
        a,b = data
        res = a*b
    if figure == 'прямоугольник':
        d,c = data
        res = d*c
    if figure == 'треугольник':
        res = (a*b)/2
    if figure == 'треугольник через высоту':
        a, h = data
        res = (a*h)/2
    if figure == 'параллелограмм':
        a,h = data
        res = a*h
    if figure == 'ромб':
        d1,d2 = data
        res = (d1*d2)/2
    return ' Площадь {} = {}'.format(figure, res)
    
figure = input('фигура >>>  ')
data = [ float(i) for i in input('данные через пробел >>> ').split()]
print(area(figure, data))