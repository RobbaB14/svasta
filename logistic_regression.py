import math
import numpy as np
# X.. matrix n*d
# Y.. vector of length n

def sigma(i,X,beta):
    x_i = -X[i]
    return (1+math.exp((x_i*beta)[0,0]))**(-1)

def log_likelihood(X, Y, beta):
    s = 0
    for i in range(len(X)):
        s += math.log(1-sigma(i,X,beta))+(Y[i]*X[i]*beta)[0,0]
    return s

def d_l(X,Y,beta):
    P = []
    for i in range(len(X)):
        p_i = sigma(i,X,beta)
        P.append(p_i)
    P = np.matrix(P)
    P = P.transpose()
    dl = X.transpose()*(Y-P)
    return dl

def dd_l(Y,X,beta):
    V = np.zeros((len(X),len(X)))
    V = np.matrix(V)
    for i in range(len(X)):
        V[i,i] = sigma(i,X,beta)*(1-sigma(i,X,beta))
    ddl = -X.transpose()*V*X
    return ddl

def my_newton(f,df,ddf,b0,tol):
    b = b0
    old_f = f(b)
    changes = True
    while changes:
        new_b = b+((ddf(b)**(-1))*df(b))
        new_f = f(new_b)
        relative_change = abs(new_f - old_f) / old_f - 1
        changes = (relative_change > tol)
        b = new_b
        old_f = new_f
    return (b)

def logistic_regression(X,Y,x):
    f = lambda beta: log_likelihood(X, Y, beta)
    df = lambda beta: d_l(X,Y,beta)
    ddf = lambda beta: dd_l(Y,X,beta)
    b0 = np.matrix((1,1,1)) # ??
    b0 = b0.transpose()
    model_beta = my_newton(f,df,ddf,b0, 10**(-8))
    prediction = sigma(0,x,model_beta)
    return(prediction)


X = np.matrix(((1,0,1),(1,1,0),(0,1,1),(0,1,0)))
Y = np.matrix((1,1,0,0))
x = np.matrix((1,0,1))
Y = Y.transpose()
print(logistic_regression(X,Y,x))

# references:
# https://statacumen.com/teach/SC1/SC1_11_LogisticRegression.pdf
# http://www.stat.cmu.edu/~cshalizi/350/lectures/26/lecture-26.pdf

