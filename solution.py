import pandas as pd
import numpy as np
from scipy import stats


chat_id = 170380561 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, p_value = stats.ks_2samp(x, y)
    return p_value < 0.02 # Ваш ответ, True или False
