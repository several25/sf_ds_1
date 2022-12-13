"""Игра угадай число"""
import numpy as np
def random_predict(number: int = np.random.randint(1, 101)) -> int:
   """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
 
   count = 0 # создаем счетчик
   max_number = 100 # задаем максимальное число
   min_number = 1 # задаем минимальное число
   predict_number = np.random.randint(1, 101) # предпологаемое число
 
   while True:
       count += 1
 
       if predict_number > number:  #если предпологаемое число больше, задаем его как максимальное
           max_number = predict_number - 1
           predict_number = (max_number + min_number) // 2
 
 
       elif predict_number < number:  #если предпологаемое число меньше, задаем его как минимальное
           min_number = predict_number + 1
           predict_number = (max_number + min_number) // 2
 
       else:
           break # игра закончена, прерываем цикл
 
   return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)