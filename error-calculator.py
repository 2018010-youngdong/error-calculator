def error(t_value,e_value):
    if e_value-t_value<0:
        print(f'{round((t_value-e_value)/t_value*100,2)}%')
    else:
        print(f'{round((e_value-t_value)/t_value*100,2)}%')

while True:
    t_value = float(input('이론값을 입력하세요 '))
    e_value = float(input('실험값을 입력하세요 '))
    error(t_value,e_value)
