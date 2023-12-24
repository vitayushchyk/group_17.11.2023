def info(*, time: float, speed: float, weight: float):
    if time < 0 or speed < 0 or weight < 0:
        raise ValueError('текст помилки - на ваш вибір')
    distance = time * speed
    result = (
        f'Транспортний засіб  {weight} кг рухався {time} секунд зі швидкістю {speed}м/сек, '
        f'і подолав відстань {distance} метрів'
    )
    return result


print(info(time=10, speed=11, weight=33))
