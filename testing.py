import pytest
from rabota import abirvalg
import math

@pytest.mark.parametrize("vvod, vivod", [
    (" ", "Вы ввели не число"),
    (0, "Тут есть деление на, 0 что неверно!"),
    ((math.pi)/2, "Тангенса пи/2 не существует"),
    (52, "Значение под корнем меньше 0"),
])

def abirvalg(vvod, vivod):
    assert abirvalg(vvod) == vivod, f"Ошибка вывода на значении {vvod}"