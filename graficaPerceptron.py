import matplotlib.pyplot as plt
#Grafica
def graph(points, weights, title):

    # Tamaño de la figura
    fig = plt.figure(figsize=(8, 6))

    # Color de fondo
    fig.set_facecolor('black')

    # Color de los ejes
    plt.rcParams['axes.linewidth'] = 2.5
    plt.rcParams['axes.edgecolor'] = 'white'

    # Color de las etiquetas de los ejes
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'

    # Tamaño de las etiquetas de los ejes
    plt.rcParams['xtick.labelsize'] = 15
    plt.rcParams['ytick.labelsize'] = 15

    # Título de la figura
    plt.title(title, fontweight='bold', color='white', fontsize=20)

    # Rango de los ejes
    plt.xlim([-5, 20])
    plt.ylim([-5, 20])

    # Graficar los puntos
    for i in points:
        if i[0] == 1:
            plt.scatter(i[1],i[2] , c='green', s=100)
        else:
            plt.scatter(i[1],i[2] , c='red', s=100, marker='^')

    # Graficar la recta
    x= [-20, 0, 20]
    # y = mx + b
    y = [(-(weights[0]/weights[2])-((weights[1]/weights[2])*x))for x in x]
   
    
    plt.plot(x, y, color = 'red', linewidth=2)
    
    #Resaltar ejes
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)

    # Mostrar la cuadrícula
    plt.grid(True)

    return 0