import numpy as np
import pandas as pd
from score_advertisers import score_advertisers, score_advertisers_power

identity = lambda x: x

def sigmoid(x):
    return 2*(1 / (1 + math.exp(-x)) - 0.5)

def sigmoid2(x):
    return 4*(1 / (1 + math.exp(-x)) - 0.5)

# scaled by mean
# above 1 means that the metric was > mean
# below 1 means that the metric was < mean
def with_mean(x, mean):
    return x * 1/mean
def with_mean_wrapper(table):
    scored = score_advertisers(table, lambda x: x)
    mean = np.mean(scored)
    return lambda x: with_mean(x, mean)

# if max sample is 1, everything stays the same
def linear_by_max(x, max_num):
    return x / max_num
def linear_by_max_wrapper(table):
    scored = score_advertisers(table, lambda x: x)
    max_num = np.max(scored)
    return lambda x: linear_by_max(x, max_num)
