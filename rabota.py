import math

def abirvalg(x):
    try:
        x = float(x)
    except ValueError:
        print("Вы ввели не число")

        a = math.sin(x)

        if x == 0: 
            raise ZeroDivisionError(f'Тут есть деление на, 0 что неверно!')
        
        if x == (math.pi / 2):
            raise ValueError(f'Тангенса пи/2 не существует')

        b = x - 2*math.cos(x)

        if b == 0:
            raise ZeroDivisionError(f'Тут первый знаменатель равен 0, что неверно!')


        d = 2*math.tan(x) - 1

        c = d/x

        if c < 0 :
            raise ValueError(f'Значение под корнем меньше 0')

        e = math.sqrt(c)

        resh = a/b + e

        print(f'Все хорошо, ваш результат {resh}')

    except ZeroDivisionError as e:
        print(f'Возникла ошибка {e}')

    except ValueError as e:
        print(f'Возникла ошибка {e}')




