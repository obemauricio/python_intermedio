def run():
    """ squares = []
    for i in range(1,101):
        if i % 3 != 0:
            squares.append(i**2)
        else:
            pass """

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]:
    #para cada i del 1 al 100 voy a guardar la i al cuadrado si y solo si la i modulo 3 es distinto de cero
    
    print(squares)

if __name__ == '__main__':
    run()