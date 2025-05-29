import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import time

# Définie une configuration aléatoire de taile N*K avec une proportion p de +1 et 1-p de -1
def Conf_Random(N,K,p):
    conf=np.zeros((N,K))
    for k in range(N):
        for l in range(K):
            conf[k][l]=2*(npr.rand()<p)-1    
    return conf    

# Calcul la différence de potentielle de deux configurations voisines (pas de potentiel pour optimiser)
def Diff_Potentiel(conf_initiale,N,K,i,j):
    diff=4*conf_initiale[i][j]*(conf_initiale[(i+1)%N][j]+conf_initiale[(i-1)%N][j]+conf_initiale[i][(j+1)%K]+conf_initiale[i][(j-1)%K])
    return diff


# Algo de Metropolis, n itérations, beta inverse de la température
def Metropolis(conf_initiale,n,beta):
    M=conf_initiale
    (N,K)=np.shape(conf_initiale)
    for k in range(n):
        i=npr.choice(range(N))
        j=npr.choice(range(K))
        u=npr.rand()
        diff=Diff_Potentiel(M,N,K,i,j)
        epsilon=1-2*(u<np.exp(- beta*diff))
        M[i][j]=epsilon*M[i][j]
    return M
    
# test
N=50
K=50 
beta=0.26
n=320000

# Evalution du temps de calul en fonction de n  (20 secondes sur mon PC ici environ)
M0=Conf_Random(N,K,0.5)
t0=time.time()
M1=Metropolis(M0,n,beta)
t1=time.time()
print(t1-t0)
# Affichage
plt.imshow(M1)


# Aimantation moyenne en fonction de beta=b, courbe théorique
def f_critique(b):
    # valeur du beta critique (transition de phase) environ 0.22
    beta_critique=0.5*np.log(1+np.sqrt(2))/2
    if (b<=beta_critique):
            y=0
    else :
        y=   np.power((1-(1/np.sinh(2*2*b))),1/8) 
    return y

# Aimantation moyenne en fonction de beta, courbe obtenue avec le thm ergodique    
# beta liste de beta
# conf de taille N*K
# n0 nombre d'itération de Metropolis partant d'une conf uniforme générant la configuration initiale
# n nombre de termes pris en compte dans la moyenne empirique (du thm ergodique) pour estimer l'aimantation moyenne en partant de la conf initiale précédente 
def Aimantation_Moyenne_Ergodic(beta,N,K,n,n0):
    L=N*K
    M0=Conf_Random(N,K,0.50)
    # C stoque les résultats pour different beta=b de l'aimantation moyenne
    C=[]
    for b in beta:
        # M Conf initiale
        M=Metropolis(M0,n0,b)
        # a aimantation moyenne de la conf initiale
        a=np.sum(M)/L
        # c aimantation moyenne cumulée initiale
        c=np.sum(M)/L
        for k in range(n):
            i=npr.choice(range(N))
            j=npr.choice(range(K))
            u=npr.rand()
            diff=Diff_Potentiel(M,N,K,i,j)
            # B=1 si on accepte la proposition, B=0 sinon
            B=(u<np.exp(- b*diff))
            # Si B=1 l'aimantation moyenne augmente ou diminue de 2/L selon qu'il y avait un -1 ou un +1 en (i,j) dans la conf précédente
            a=a+B*(2*(M[i][j]<0)-1)*(2/L)
            # on incrémente l'aimantation cumulée
            c=c+a
            # On met à jour la nouvelle configuration 
            epsilon=1-2*(u<np.exp(- b*diff))
            M[i][j]=epsilon*M[i][j]
        # On fait la moyenne de l'aimantation cumulée (simme de n+1 termes dans le thm ergodique)    
        C.append(np.abs(c)/(n+1))
    # On affiche la courbe théorique
    beta_min=np.min(beta)
    beta_max=np.max(beta)
    
    t=np.linspace(np.max(beta_min-0.1,0),beta_max+0.1,100)
    y=[]
    for b in t:
        y.append(f_critique(b))
    
    plt.plot(t,y)            
    # On affiche les points expérimentaux
    plt.scatter(beta,C, label='Points', color='blue', marker='o')    
    plt.show()    
    
# test (260 secondes sur pc bureau)
t0=time.time()            
Aimantation_Moyenne_Ergodic([0.1,0.2,0.25,0.3,0.35],50,50,320000,320000)            
t1=time.time()
print(t1-t0)    


