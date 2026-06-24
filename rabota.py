import math

def abirvalg(z):

    try:
        x = float(z)
    except ValueError:
        return "Вы ввели не число"
    
    else:
        try:
            (2*math.tan(x) - 1) /x
        except ZeroDivisionError:
            return "Тут есть деление на, 0 что неверно!"
        else:
            try:
                math.sqrt((2*math.tan(x) - 1)/x)
            except ValueError:
                return "Значение под корнем меньше 0"
            else:

                a = math.sin(x)

                b = x - 2*math.cos(x)

                d = 2*math.tan(x) - 1

                c = d/x

                e = math.sqrt(c)

                a/b + e

                return "Все хорошо"

def main():
    z = input('Введите число: ')
    b = abirvalg(z)
    print(b)
if __name__ == "__main__":
    main()
