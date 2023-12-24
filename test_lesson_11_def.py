import pytest

import lesson_11_def


def test_info():
    result = lesson_11_def.info(time=2, speed=5, weight=7)
    expect_result = 'Транспортний засіб  7 кг рухався 2 секунд зі швидкістю 5м/сек, і подолав відстань 10 метрів'
    assert result == expect_result


def test_info_bad_input():
    with pytest.raises(ValueError):
        lesson_11_def.info(time=-6, speed=5, weight=7)
