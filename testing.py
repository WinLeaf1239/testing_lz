import pytest
import math
from rabota import abirvalg 

@pytest.fixture
def variki():
    # Ключ — текстовое описание, значение — кортеж (число x, какую фразу мы ждем в принте)
    return {
        "Без перехвата": (67, "Все хорошо"),
        "Перехват на 0": (0, "Тут есть деление на, 0 что неверно!"),
        "Перехват на отриц знач под корнем": (52, "Значение под корнем меньше 0")
    }


#capsys перехватывает вывод в терминале
def test_abirvalg(variki, capsys):
    for fir, znach in variki.items():
        
        x, text = znach
        
        abirvalg(x)
        
        #capsys.readouterr() перехватывает все что вывелось
        viv = capsys.readouterr()
        
        #Проверка, viv.out - текст который выда принт
        assert text in viv.out, f'Возника ошибка, для группы {fir} программа сделала ошибку'

if __name__ == '__main__':
    pytest.main([__file__, "-v"])