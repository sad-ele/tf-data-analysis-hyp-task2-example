import pandas as pd
import numpy as np
from scipy import stats


chat_id = 170380561 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    return (stats.anderson_ksamp([x, y]).significance_level < 0.02)

