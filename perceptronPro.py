import matplotlib.pyplot as plt
import graficaPerceptron 

def main():
    
    #parametros iniciales sugeridos
    initial_weights = [0, -0.5, 2] 
    rate_n = 0.2
    iter_max = 2000
   
    points = [
                [0, 14, 2], [0,16, 5], [0,17, 10], [0,19, 3],[0,14,18],
                [1,6, 9], [1, 8, 14], [1, 9, 7], [1, 9, 11], [1, 11, 8], 
             ]
    
    fianl_weights, current_iter= perceptron(initial_weights, points, rate_n, iter_max)

    # Mostrar el gráfico
    graficaPerceptron.graph(points, initial_weights, "Initial weights")
    graficaPerceptron.graph(points, fianl_weights, "Resulting weights")

    print(initial_weights)
    print(fianl_weights)
    print(current_iter)
    
    plt.show()
    

#salida del perceptron 
# 1 -> p(sumatoria)>0
# 0 -> p(sumatoria)<=0
def perceptron_output(weights, point):
    #producto punto 
    summation = (weights[0]*1 + weights[1]*point[1] + weights[2]*point[2])
    if summation > 0:
        return 1
    else:
        return 0


def new_weights(weights, point, rate_n, change_weight):
    # salida del perceptron
    perceptron_out = perceptron_output(weights, point)
    
    # calcular escalar
    num = rate_n * (point[0] - perceptron_out)

    # si scalar es 0 retorna de una ves el mismo peso y omite mas calculos
    if num == 0:
        return weights, change_weight

    # asignando nuevo vector
    new_weights = [w + num * p for w, p in zip(weights, point)]
        #new_weights[0] = new_weights[0] + (scalar * point[0])

    # verificando si vector cambio
    if (weights != new_weights):
        change_weight += 1

    return new_weights, change_weight


def perceptron (weights, points, rate_n, max_iter):

    current_weights = list(weights)
    current_iter = 0
    change_weight = 1

    # mientras realice todas las iteraciones o ya haya aprendido 
    while current_iter < max_iter and change_weight != 0:
        change_weight = 0
        # hayando nuevos pesos para cada punto
        for point in points:
            current_weights, change_weight = new_weights(current_weights, point, rate_n, change_weight)
        current_iter += 1
        if current_iter == max_iter:
            print(" !! No se encontro solucion para clasificar este caso")
    return current_weights, current_iter


if __name__ == "__main__":
    main()
    
