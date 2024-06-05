#Простейшая нейронная сеть с несколькими точками данных (входами)

toes = [8.5, 9.5, 9.9, 9.0] #среднее число игр, сыгранных игроками
wlrec = [0.65, 0.8, 0.8, 0.9] #доля игр, окончившихся победой(процент)
nfans = [1.2, 1.3, 0.5, 1.0] #число болельщиков (в миллионах)
input = [toes[0], wlrec[0], nfans[0]] #Запись первой игры в сезоне

weights = [0.1, 0.2, 0] #весовой коэффициент

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] + b[i])
    return output

def neural_network(input, weights):
    pred = w_sum(input, weights)
    return pred

pred = neural_network(input=input, weights=weights)
print(pred)
