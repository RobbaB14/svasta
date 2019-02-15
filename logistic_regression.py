import math
import numpy as np
# X.. matrix n*d
# Y.. vector of length n

def sigma(i,X,beta):
    x_i = -X[i]
    return (1+np.exp((x_i*beta)[0,0]))**(-1)

def log_likelihood(X, Y, beta):
    s = 0
    for i in range(len(X)):
        s += math.log(1-sigma(i,X,beta))+(Y[0,i]*X[i]*beta)[0,0]
    return s

def d_l(X,Y,beta):
    P = []
    for i in range(len(X)):
        p_i = sigma(i,X,beta)
        P.append(p_i)
    P = np.matrix(P).transpose()
    Y = Y.transpose()
    dl = X.transpose()*(Y-P)
    return dl

def dd_l(Y,X,beta):
    V = np.zeros((len(X),len(X)))
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

def logistic_regression(X,Y,x,X_test,treshold):
    f = lambda beta: log_likelihood(X,Y,beta)
    df = lambda beta: d_l(X,Y,beta)
    ddf = lambda beta: dd_l(Y,X,beta)
    b0 = x
    model_beta = my_newton(f,df,ddf,b0,10**(-8)).transpose()
    Y_prediction = []
    for i in range(len(X_test)):
        prediction = sigma(i, X_test, model_beta.transpose())
        if prediction > treshold:
            Y_prediction.append(1)
        else:
            Y_prediction.append(0)
        # Y_prediction.append(sigma(i, X_test, model_beta.transpose()))

    # dY = Y_prediction-Y_test
    # approx_mis = dY.sum()/dY.shape[1]
    return(Y_prediction)

def evaluation(Y_prediction, Y_test):
    Y_prediction = np.matrix(Y_prediction)
    Y_test = np.matrix(Y_test)
    TN = np.count_nonzero(Y_test + Y_prediction==0)
    TP = np.count_nonzero(np.multiply(Y_test, Y_prediction)==1)
    FP = np.count_nonzero(Y_test - Y_prediction==-1)
    FN = np.count_nonzero(Y_test - Y_prediction==1)
    print(TP, FP, FN, TN)
    precision = TP / (TP+FP)
    recall = TP / (TP+FN)

    F1 = (2*precision*recall)/(precision+recall)
    # print(TP, FP, FN, TN)
    return (precision, recall, F1)



# imput:
X_vec = []
Y_vec = []
data = open('iris_data.txt', 'r')
line = data.readline().split(',')
while len(line)>1:
    vect = line[0:3]
    X_vec.append([float(c) for c in vect[0:3]])
    if line[4] == 'Iris-setosa\n':
        Y_vec.append(1)
    else:
        Y_vec.append(0)
    line = data.readline().split(',')
data.close()
X = np.matrix(X_vec[0:100])
X_test = np.matrix(X_vec[100:151])
Y = np.matrix(Y_vec[0:100])
Y_test = np.matrix(Y_vec[100:151])
x = np.matrix((0, 1, -1)).transpose()

treshold = 0.7


Y_prediction = logistic_regression(X,Y,x,X_test,treshold)
(precision, recall, F1)= evaluation(Y_prediction, Y_test)
print('precision:', precision, ', recall:', recall, ', F1:', F1)