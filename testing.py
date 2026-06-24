import pytest
from rabota import abirvalg

@pytest.mark.parametrize("vvod, vivod", [
    (" ", "Вы ввели не число"),
    (0, "Тут есть деление на, 0 что неверно!"),
    (52, "Значение под корнем меньше 0"),
])


def test_abirvalg(vvod, vivod):
    assert abirvalg(vvod) == vivod, f"Ошибка вывода на значении {vvod}"
    
if __name__ == "__main__":
    pytest.main([__file__, "-v"])