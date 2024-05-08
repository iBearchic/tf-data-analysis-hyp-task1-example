import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 539822853 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Нулевая гипотеза: нет различий между долями успехов
    # Альтернативная гипотеза: различия есть
    
    # Количество успехов и общее количество наблюдений
    successes = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    
    # z-тест для двух пропорций
    z_stat, p_value = proportions_ztest(successes, nobs, alternative='two-sided')
    
    # Уровень значимости
    alpha = 0.05
    
    # Если p-значение меньше alpha, отклоняем нулевую гипотезу
    return p_value < alpha
