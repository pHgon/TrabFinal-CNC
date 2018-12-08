import math

def ourFunction(x):
    return math.pow(math.e, 4 - math.pow(x, 2))

def analytical(a, b):
    # e^4 * -1/2x * e^(-x^2)
    e1 = math.pow(math.e, 4) * (-1.0 / (2.0*b)) * math.pow(math.e, -1 * math.pow(b, 2))
    e2 = math.pow(math.e, 4) * (-1.0 / (2.0*a)) * math.pow(math.e, -1 * math.pow(a, 2))
    return str(e1-e2)[0:7]

def trapezio(a, b, n):
    h = (b - a)/n
    result = ourFunction(a) + ourFunction(b)
    for i in range(1, n):
        result += 2 * ourFunction(a + h*i)

    return h/2 * result

def simp1Por3(a, b, n):
    h = (b - a)/n

    result = ourFunction(a) + ourFunction(b)
    for i in range(1, n):
        if i % 2 == 0:
            t = 2
        else:
            t = 4
        result += t * ourFunction(a + h * i)

    return h/3 * result

def simp3Por8(a, b, n):
    h = (b - a)/n

    result = ourFunction(a) + ourFunction(b)
    for i in range(1, n):
        if i % 3 == 0:
            t = 2
        else:
            t = 3
        result += t * ourFunction(a + h * i)

    return 3*h/8 * result

a = 2
b = 5
solucaoSimples = float(analytical(a, b))
print("Solucao analitica:\t" + str(solucaoSimples))

print("\nTrapezio Repetida")
qtdeIteracoes = 10
trapezio = trapezio(a, b, qtdeIteracoes)
trapezioErroAbsoluto = abs(solucaoSimples - trapezio)
print("\tResultado com 10 subintervalos: \t" + str(round(trapezio, 5)))
print("\tErro relativo:\t" + str(round(trapezioErroAbsoluto, 5)))


print("\n1/3 de Simpson Repetida")
simpson1Por3 = simp1Por3(a, b, qtdeIteracoes)
simpson1Por3ErroAbsoluto = abs(solucaoSimples - simpson1Por3)
print("\tResultado com 10 subintervalos: \t" + str(round(simpson1Por3, 5)))
print("\tErro relativo:\t" + str(round(simpson1Por3ErroAbsoluto, 5)))

print("\n3/8 de Simpson Repetida")
simpson3Por8 = simp3Por8(a, b, qtdeIteracoes)
simpson3Por8ErroAbsoluto = abs(solucaoSimples - simpson1Por3)
print("\tResultado com 10 subintervalos: \t" + str(round(simpson3Por8, 5)))
print("\tErro relativo:\t" + str(round(simpson3Por8ErroAbsoluto, 5)))
