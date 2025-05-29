#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:05:20 2025

@author: yoffret
"""

# alpha, beta paramètres du pas eps,  K nombre d'itération,  p nombres de paramètres à estimer, 
# stoqués dans theta, N nombre de données par variables
# loc_grad initialisé à zero, représente le gradient courant
# les donnés sont stoqués dans une matrice N*p data_new
for i in range(K):
    eps=alpha/(1+(i/beta))
    k=np.random.randint(0,N)
    y_cancer=cancer_status[k]
    Logit=theta[0]
    data_k=data_new[k,:]
    for j in range(p-1):
        Logit += theta[j+1] * data_k[j]
    C=-y_cancer/(1+np.exp(+y_cancer*Logit))
    loc_grad[0]=C
    for j in range(p-1):
        loc_grad[j+1]=C*data_k[j]
    theta= theta-eps*loc_grad

    


