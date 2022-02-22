# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 19:54:04 2022

"""

import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF
from tqdm import tqdm

 
class EmpiricalDistribution:

    """
    Class for empirical distriution computation
    """

    def __init__(self):
        self.ecdf_estimator = {}
        self.unique_values = {}

       
    def fit_transform(self, data, columns):
        self.data = data
        self.columns = columns
        self.dtype = data.dtypes
        for col in columns:
            self.ecdf_estimator[col] = ECDF(data[col])
            self.unique_values[col] = np.unique(data[col])
            self.data[col] = self.ecdf_estimator[col](data[col])
        return data

    def inverse_transform(self, new_data):
        for col in tqdm(self.columns):
            associated_value = []
            for new_prob in new_data[col]:
                last_prob = 0
                for prob, value in zip(np.unique(self.data[col]), self.unique_values[col]):
                    if (new_prob >= last_prob) & (new_prob <= prob):
                        associated_value.append(value)
                        break
                    last_prob = prob
            new_data[col] = associated_value
        return new_data[self.columns].astype(self.dtype[self.columns])
    
    