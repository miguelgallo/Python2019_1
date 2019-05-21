import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.optimize import curve_fit
from scipy.special import erf
from scipy.stats import chi2
from scipy.stats import chisquare
from scipy.stats import power_divergence

ds = pd.read_csv('DoubleMuRun2011A.csv')
print(ds.head())

invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2) ))
print('Os primeiros cinco valores calculados (em unidades GeV)')
print(invariant_mass[0:5])

# Limitando o ajuste próximo ao pico do histograma.
escolha = 0
expected = 0
while(escolha>4 or escolha<1):
    escolha = int(input("Escolha 1, 2, 3 ou 4: Enter 1 --> Z, Enter 2 --> Upsilon, Enter 3 --> J/Psi ou Enter 4 --> Psi':  "))
    #escolha = int(escolha)
    if escolha == 1:
        lowerlimit = 70
        upperlimit = 110
        expected = 91.1876
         
    elif escolha == 2:
        lowerlimit = 9.15
        upperlimit = 9.75
        expected = 9.46030
         
    elif escolha == 3:
        lowerlimit = 2.95
        upperlimit = 3.2
        expected = 3.096916
        
    else:
        lowerlimit = 3.55
        upperlimit = 3.78
        expected = 3.686111
        

bins = int(input('Insira a binagem desejada: '))

# Selecionando os valores de massa invariante que estão dentro das limitações.
limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Criando um histograma com os valores selecionados.
histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))

# No eixo y, o número de eventos para cada bin (pode ser obtido a partir da variável histograma).
# No eixo x, centro das classes.
y = histogram[0]
x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )

# Definindo funções para os ajustes
def expo(x, const, slope):
    """ Uma curva exponencial. 
  parametros: const, slope """
    return np.exp(const + slope*x)

def line(x, intercept, slope):
    """ Polinômio do primeiro grau. """
    return slope*x + intercept

def breitwigner(E, gamma, M, a, b, A):
    ''' E (é a energia)
        gamma (a largura total do meio no máximo da distribuição)
        M (valor onde ocorre o máximo da distribuição)
        a (inclinação que é usada para pereber o efeito de backgrund)
        b (intercepção em y, que é usada para perceber o efeito de background)
        A ("amplitude" da distribuição de Breit-Wigner) '''
    return a*E+b+A*( (2*np.sqrt(2)*M*gamma*np.sqrt(M**2*(M**2+gamma**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gamma**2)))) )/((E**2-M**2)**2+M**2*gamma**2)

def gaussian(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def doublegaussian(x, a1, x01, sigma1, a2, x02, sigma2):
    return a1*np.exp(-(x-x01)**2/(2*sigma1**2))+a2*np.exp(-(x-x02)**2/(2*sigma2**2))

def crystalball(x, a, n, xb, sig):
    x = x+0j
    #N, a, n, xb, sig = parametros
    if a < 0:
        a = -a
    if n < 0:
        n = -n
    aa = abs(a)
    A = (n/aa)**n * np.exp(- aa**2 / 2)
    B = n/aa - aa
    C = n/aa / (n-1.) * np.exp(-aa**2/2.)
    D = np.sqrt(pi/2.) * (1. + erf(aa/np.sqrt(2.)))
    N = 1. / (sig * (C+D))
    total = 0.*x
    total += ((x-xb)/sig  > -a) * N * np.exp(- (x-xb)**2/(2.*sig**2))
    total += ((x-xb)/sig <= -a) * N * A * (B - (x-xb)/sig)**(-n)
    try:
      return total.real

    except:
      return total
    return total

def crystalexpo(x, a, n, xb, sig, const, slope): #6 parâmetros
    return (crystalball(x, a, n, xb, sig)+expo(x, const, slope))

def doublecrystal(x, a1, n1, xb1, sig1, a2, n2, xb2, sig2): #8 parâmetros
    return (crystalball(x, a1, n1, xb1, sig1)+crystalball(x, a2, n2, xb2, sig2))

def doublecrystalexpo(x, a1, n1, xb1, sig1, a2, n2, xb2, sig2, const, slope): #10 parâmetros
    return(doublecrystal(x, a1, n1, xb1, sig1, a2, n2, xb2, sig2)+expo(x, const, slope))

def doublegaussianexpo(x, a1, x01, sigma1, a2, x02, sigma2, const, slope): #8 parâmetros
    return (doublegaussian(x, a1, x01, sigma1, a2, x02, sigma2)+expo(x, const, slope))

def crystalgaussianexpo(x, a1, n1, xb1, sig1, a, x0, sigma, const, slope): #10 parâmetros
    return (crystal(x, a1, n1, xb1, sig1)+gaussian(x, a, x0, sigma)+expo(x, const, slope))

# Valores iniciais para a otimização na seguinte ordem: [gamma, M, a, b, A]

initials_breit = 0
initials_gauss = 0
initials_crystal = 0
initials_upsilon = 0
choice = 0
i = 0

if escolha == 1:
    print("gamma (a largura total do meio no máximo da distribuição),\nM(valor onde ocorre o máximo da distribuição),\na (inclinação que é usada para pereber o efeito de backgrund),\nb (intercepção em y, que é usada para perceber o efeito de background),\nA (amplitude da distribuição de Breit-Wigner)")
    initials_breit =  [float(x) for x in input('Preencha com os parâmetros da Briet-Wigner (gamma, M, a, b, A) dando apenas espaços entre eles: ').split()] #Para o Z:[4, 91, -2, 150, 13000]
    # Vamos importar o módulo que é usado na otimização, executar a otimização e calcular as incertezas dos parâmetros otimizados.
    best_breit, covariance = curve_fit(breitwigner, x, y, p0=initials_breit, sigma=np.sqrt(y))
    error_breit = np.sqrt(np.diag(covariance))

    # Vamos imprimir os valores e incertezas obtidos com a otimização.
    print("Valores com incertezas")
    print("")
    first = "Valor da largura de decaimento (gamma) = {} +- {}".format(best_breit[0], error_breit[0])
    second = "Valor do pico da distribuição (M) = {} +- {}".format(best_breit[1], error_breit[1])
    third = "a = {} +- {}".format(best_breit[2], error_breit[2])
    fourth = "b = {} +- {}".format(best_breit[3], error_breit[3])
    fifth = "A = {} +- {}".format(best_breit[4], error_breit[4])
    #chi2_norm = chi2.pdf(x, best_breit)/(bins - num_breit)                         
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)
    #print(chi2_norm)

    # Diferença entre os valores iniciais e o melhor valor após o 1º curve_fit
    dif_breit = [np.absolute(best_breit[0] - initials_breit[0]), np.absolute(best_breit[1] - initials_breit[1]), np.absolute(best_breit[2] - initials_breit[2]), np.absolute(best_breit[3] - initials_breit[3]), np.absolute(best_breit[4] - initials_breit[4])]

    # Interação para convergir para o melhor valor dos parâmetros
    while (dif_breit[0] > 0 and dif_breit[1] > 0 and dif_breit[2] > 0 and dif_breit[3] > 0 and dif_breit[4] > 0 and i <= 14):
        initials_breit = [best_breit[0], best_breit[1], best_breit[2], best_breit[3], best_breit[4]]
        best_breit, covariance = curve_fit(breitwigner, x, y, p0=initials_breit, sigma=np.sqrt(y))
        error_breit = np.sqrt(np.diag(covariance))
        first = "Valor da largura de decaimento (gamma) = {} +- {}".format(best_breit[0], error_breit[0])
        second = "Valor do pico da distribuição (M) = {} +- {}".format(best_breit[1], error_breit[1])
        third = "a = {} +- {}".format(best_breit[2], error_breit[2])
        fourth = "b = {} +- {}".format(best_breit[3], error_breit[3])
        fifth = "A = {} +- {}".format(best_breit[4], error_breit[4])
        print(first)
        print(second)
        print(third)
        print(fourth)
        print(fifth)
        dif_breit = [np.absolute(best_breit[0] - initials_breit[0]), np.absolute(best_breit[1] - initials_breit[1]), np.absolute(best_breit[2] - initials_breit[2]), np.absolute(best_breit[3] - initials_breit[3]), np.absolute(best_breit[4] - initials_breit[4])]
        i += 1
        print("Interação número: ", i)

    print("Número de iterações: ", i)
    if (i == 1):
        print("O fit ficou bom? Legal! \nNão ficou? Tente outros valores iniciais! ")
    elif (i >= 1 and i <= 13):
        print("O fit convergiu!")
    else:
        print("O fit provavelmente está divergindo... Tente outros valores iniciais!")

    print(chisquare(y, breitwigner(x, best_breit[0], best_breit[1], best_breit[2], best_breit[3], best_breit[4])))
    print(power_divergence(y, breitwigner(x, 4, 91, -2, 150, 13000), lambda_="neyman"))
    plt.plot(x, breitwigner(x, *best_breit), 'r-', label='gamma = {}, M = {}'.format(best_breit[0], best_breit[1]))
    plt.xlabel('Massa Invariante [GeV]')
    plt.ylabel('Número de Eventos')
    plt.title('Bóson Z: Ajuste com Breit-Wigne')
    plt.legend()    
    plt.show()


elif escolha == 2:
    print("gamma (a largura total do meio no máximo da distribuição),\nM(valor onde ocorre o máximo da distribuição),\na (inclinação que é usada para pereber o efeito de backgrund),\nb (intercepção em y, que é usada para perceber o efeito de background),\nA (amplitude da distribuição de Breit-Wigner)")
    initials_upsilon =  [float(x) for x in input('Preencha com os parâmetros das duas CrystalBall e da exponencial (a1, n1, mean1, sigma1, a2, n2, mean2, sigma2, constante, inclinação) dando apenas espaços entre eles: ').split()] #Para o Upsilon: [0.2 9.5 50 -370 180]
    # Vamos importar o módulo que é usado na otimização, executar a otimização e calcular as incertezas dos parâmetros otimizados.
    best_upsilon, covariance = curve_fit(doublecrystalexpo, x, y, p0=initials_upsilon, sigma=np.sqrt(y))
    error_upsilon = np.sqrt(np.diag(covariance))

    # Vamos imprimir os valores e incertezas obtidos com a otimização.
    print("Valores com incertezas")
    print("")
    primeiro = "Valor de a1 = {} +- {}".format(best_upsilon[0], error_upsilon[0])
    segundo = "Valor de n1 = {} +- {}".format(best_upsilon[1], error_upsilon[1])
    terceiro = "Valor de mean1 = {} +- {}".format(best_upsilon[2], error_upsilon[2])
    quarto = "Valor de sigma1 = {} +- {}".format(best_upsilon[3], error_upsilon[3])
    quinto = "Valor de a2 = {} +- {}".format(best_upsilon[4], error_upsilon[4])
    sexto = "Valor de n2 = {} +- {}".format(best_upsilon[5], error_upsilon[5])
    setimo = "Valor de mean2 = {} +- {}".format(best_upsilon[6], error_upsilon[6])
    oitavo = "Valor de sigma2 = {} +- {}".format(best_upsilon[7], error_upsilon[7])
    nono = "Valor da constante = {} +- {}".format(best_upsilon[8], error_upsilon[8])
    decimo = "Valor da inclinação = {} +- {}".format(best_upsilon[9], error_upsilon[9])
    print(primeiro)
    print(segundo)
    print(terceiro)
    print(quarto)
    print(quinto)
    print(sexto)
    print(setimo)
    print(oitavo)
    print(nono)
    print(decimo)

    # Diferença entre os valores iniciais e o melhor valor após o 1º curve_fit
    dif_upsilon = [np.absolute(best_upsilon[0] - initials_upsilon[0]), np.absolute(best_upsilon[1] - initials_upsilon[1]),  np.absolute(best_upsilon[2] - initials_upsilon[2]), np.absolute(best_upsilon[3] - initials_upsilon[3]), np.absolute(best_upsilon[4] - initials_upsilon[4]), np.absolute(best_upsilon[5] - initials_upsilon[5]), np.absolute(best_upsilon[6] - initials_upsilon[6]), np.absolute(best_upsilon[7] - initials_upsilon[7]), np.absolute(best_upsilon[8] - initials_upsilon[8]), np.absolute(best_upsilon[9] - initials_upsilon[9])]

    # Interação para convergir para o melhor valor dos parâmetros
    while (dif_upsilon[0] > 0 and dif_upsilon[1] > 0 and dif_upsilon[2] > 0 and dif_upsilon[3] > 0 and dif_upsilon[4] > 0 and dif_upsilon[5] > 0 and dif_upsilon[6] > 0 and dif_upsilon[7] > 0 and dif_upsilon[8] > 0 and dif_upsilon[9] > 0 and i <= 14):
        initials_upsilon = [best_upsilon[0], best_upsilon[1], best_upsilon[2], best_upsilon[3], best_upsilon[4], best_upsilon[5], best_upsilon[6], best_upsilon[7], best_upsilon[8], best_upsilon[9]]
        best_upsilon, covariance = curve_fit(doublecrystalexpo, x, y, p0=initials_upsilon, sigma=np.sqrt(y))
        error_upsilon = np.sqrt(np.diag(covariance))
        primeiro = "Valor de a1 = {} +- {}".format(best_upsilon[0], error_upsilon[0])
        segundo = "Valor de n1 = {} +- {}".format(best_upsilon[1], error_upsilon[1])
        terceiro = "Valor de mean1 = {} +- {}".format(best_upsilon[2], error_upsilon[2])
        quarto = "Valor de sigma1 = {} +- {}".format(best_upsilon[3], error_upsilon[3])
        quinto = "Valor de a2 = {} +- {}".format(best_upsilon[4], error_upsilon[4])
        sexto = "Valor de n2 = {} +- {}".format(best_upsilon[5], error_upsilon[5])
        setimo = "Valor de mean2 = {} +- {}".format(best_upsilon[6], error_upsilon[6])
        oitavo = "Valor de sigma2 = {} +- {}".format(best_upsilon[7], error_upsilon[7])
        nono = "Valor da constante = {} +- {}".format(best_upsilon[8], error_upsilon[8])
        decimo = "Valor da inclinação = {} +- {}".format(best_upsilon[9], error_upsilon[9])
        print(primeiro)
        print(segundo)
        print(terceiro)
        print(quarto)
        print(quinto)
        print(sexto)
        print(setimo)
        print(oitavo)
        print(nono)
        print(decimo)
        dif_upsilon = [np.absolute(best_upsilon[0] - initials_upsilon[0]), np.absolute(best_upsilon[1] - initials_upsilon[1]),  np.absolute(best_upsilon[2] - initials_upsilon[2]), np.absolute(best_upsilon[3] - initials_upsilon[3]), np.absolute(best_upsilon[4] - initials_upsilon[4]), np.absolute(best_upsilon[5] - initials_upsilon[5]), np.absolute(best_upsilon[6] - initials_upsilon[6]), np.absolute(best_upsilon[7] - initials_upsilon[7]), np.absolute(best_upsilon[8] - initials_upsilon[8]), np.absolute(best_upsilon[9] - initials_upsilon[9])]
        i += 1
        print("Interação número: ", i)

    print("Número de iterações: ", i)
    if (i == 1):
        print("O fit ficou bom? Legal! \nNão ficou? Tente outros valores iniciais! ")
    elif (i >= 1 and i <= 13):
        print("O fit convergiu!")
    else:
        print("O fit provavelmente está divergindo... Tente outros valores iniciais!")

    plt.plot(x, doublecrystalexpo(x, *best_upsilon), 'r-')
    plt.xlabel('Massa Invariante [GeV]')
    plt.ylabel('Número de Eventos')
    plt.title('Upsilon: Ajuste com Dupla CrystalBall + Exponencial')
    plt.legend()
    plt.show()

elif escolha == 4:
    print("a (define como a função decresce no pico), \n n (), \n mean (mean, ordena a posição do centro do pico), \n sigma (desvio padrão, controla a largura da curva)")
    initials_psiprime =  [float(x) for x in input('Preencha com os parâmetros da Crystal-Ball  (a, n, mean, sigma): ').split()] #Para o Psi-prime: [-1 3.7 -10 100 -10]
    print("a (define como a função decresce no pico), \n n (), \n mean (mean, ordena a posição do centro do pico), \n sigma (desvio padrão, controla a largura da curva)")
    initials_crystal =  [float(x) for x in input('Preencha com os parâmetros da Crystal-Ball  (a, n, mean, sigma): ').split()]#Para J/Psi: [2 0.5 3.5 1] 
    # Vamos importar o módulo que é usado na otimização, executar a otimização e calcular as incertezas dos parâmetros otimizados.
    best_crystal, covariance = curve_fit(crystalball, x, y, p0=initials_crystal, sigma=np.sqrt(y))
    error_crystal = np.sqrt(np.diag(covariance))

    # Vamos imprimir os valores e incertezas obtidos com a otimização.
    print("Valores com incertezas")
    print("")
    first = "Valor de a = {} +- {}".format(best_crystal[0], error_crystal[0])
    second = "Valor de n = {} +- {}".format(best_crystal[1], error_crystal[1])
    third = "Valor de mean = {} +- {}".format(best_crystal[2], error_crystal[2])
    fourth = "Value de sigma = {} +- {}".format(best_crystal[3], error_crystal[3])
    #chi2 = (((best_crystal[2]-expected)**2)/best_crystal[2]).sum()
    print(first)
    print(second)
    print(third)
    print(fourth)
    #print("chi2: ", chi2)

    # Diferença entre os valores iniciais e o melhor valor após o 1º curve_fit
    dif_crystal = [np.absolute(best_crystal[0] - initials_crystal[0]), np.absolute(best_crystal[1] - initials_crystal[1]), np.absolute(best_crystal[2] - initials_crystal[2]), np.absolute(best_crystal[3] - initials_crystal[3])]

    # Interação para convergir para o melhor valor dos parâmetros
    while (dif_crystal[0] > 0 and dif_crystal[1] > 0 and dif_crystal[2] > 0 and dif_crystal[3] > 0 and i <= 14):
        initials_crystal = [best_crystal[0], best_crystal[1], best_crystal[2], best_crystal[3]]
        best_crystal, covariance = curve_fit(crystalball, x, y, p0=initials_crystal, sigma=np.sqrt(y))
        error_crystal = np.sqrt(np.diag(covariance))
        first = "Valor de a = {} +- {}".format(best_crystal[0], error_crystal[0])
        second = "Valor de n = {} +- {}".format(best_crystal[1], error_crystal[1])
        third = "Valor de mean = {} +- {}".format(best_crystal[2], error_crystal[2])
        fourth = "Valor de sigma = {} +- {}".format(best_crystal[3], error_crystal[3])
        print(first)
        print(second)
        print(third)
        print(fourth)
        dif_crystal = [np.absolute(best_crystal[0] - initials_crystal[0]), np.absolute(best_crystal[1] - initials_crystal[1]), np.absolute(best_crystal[2] - initials_crystal[2]), np.absolute(best_crystal[3] - initials_crystal[3])]
        i += 1
        print("Interação número: ", i)

    print("Número de iterações: ", i)
    if (i == 1):
        print("O fit ficou bom? Legal! \nNão ficou? Tente outros valores iniciais! ")
    elif (i >= 1 and i <= 13):
        print("O fit convergiu!")
    else:
        print("O fit provavelmente está divergindo... Tente outros valores iniciais!")

    plt.plot(x, crystalball(x, *best_crystal), 'r-', label='mean = {}, sigma = {}'.format(best_crystal[2], best_crystal[3]))
    plt.xlabel('Massa Invariante [GeV]')
    plt.ylabel('Número de Eventos')
    plt.title('Psi-prime: Ajuste com CrystalBall')
    plt.legend()
    plt.show()
        
else:
    print("a (define como a função decresce no pico), \n n (), \n mean (mean, ordena a posição do centro do pico), \n sigma (desvio padrão, controla a largura da curva)")
    initials_crystal =  [float(x) for x in input('Preencha com os parâmetros da Crystal-Ball  (a, n, mean, sigma): ').split()]#Para J/Psi: [2 0.5 3.5 1] 
    # Vamos importar o módulo que é usado na otimização, executar a otimização e calcular as incertezas dos parâmetros otimizados.
    best_crystal, covariance = curve_fit(crystalball, x, y, p0=initials_crystal, sigma=np.sqrt(y))
    error_crystal = np.sqrt(np.diag(covariance))

    # Vamos imprimir os valores e incertezas obtidos com a otimização.
    print("Valores com incertezas")
    print("")
    first = "Valor de a = {} +- {}".format(best_crystal[0], error_crystal[0])
    second = "Valor de n = {} +- {}".format(best_crystal[1], error_crystal[1])
    third = "Valor de mean = {} +- {}".format(best_crystal[2], error_crystal[2])
    fourth = "Value de sigma = {} +- {}".format(best_crystal[3], error_crystal[3])
    #chi2 = (((best_crystal[2]-expected)**2)/best_crystal[2]).sum()
    print(first)
    print(second)
    print(third)
    print(fourth)
    #print("chi2: ", chi2)

    # Diferença entre os valores iniciais e o melhor valor após o 1º curve_fit
    dif_crystal = [np.absolute(best_crystal[0] - initials_crystal[0]), np.absolute(best_crystal[1] - initials_crystal[1]), np.absolute(best_crystal[2] - initials_crystal[2]), np.absolute(best_crystal[3] - initials_crystal[3])]

    # Interação para convergir para o melhor valor dos parâmetros
    while (dif_crystal[0] > 0 and dif_crystal[1] > 0 and dif_crystal[2] > 0 and dif_crystal[3] > 0 and i <= 14):
        initials_crystal = [best_crystal[0], best_crystal[1], best_crystal[2], best_crystal[3]]
        best_crystal, covariance = curve_fit(crystalball, x, y, p0=initials_crystal, sigma=np.sqrt(y))
        error_crystal = np.sqrt(np.diag(covariance))
        first = "Valor de a = {} +- {}".format(best_crystal[0], error_crystal[0])
        second = "Valor de n = {} +- {}".format(best_crystal[1], error_crystal[1])
        third = "Valor de mean = {} +- {}".format(best_crystal[2], error_crystal[2])
        fourth = "Valor de sigma = {} +- {}".format(best_crystal[3], error_crystal[3])
        print(first)
        print(second)
        print(third)
        print(fourth)
        dif_crystal = [np.absolute(best_crystal[0] - initials_crystal[0]), np.absolute(best_crystal[1] - initials_crystal[1]), np.absolute(best_crystal[2] - initials_crystal[2]), np.absolute(best_crystal[3] - initials_crystal[3])]
        i += 1
        print("Interação número: ", i)

    print("Número de iterações: ", i)
    if (i == 1):
        print("O fit ficou bom? Legal! \nNão ficou? Tente outros valores iniciais! ")
    elif (i >= 1 and i <= 13):
        print("O fit convergiu!")
    else:
        print("O fit provavelmente está divergindo... Tente outros valores iniciais!")

    print(chisquare(y, crystalball(x, best_crystal[0], best_crystal[1], best_crystal[2], best_crystal[3])))
    print(power_divergence(y, crystalball(x, best_crystal[0], best_crystal[1], best_crystal[2], best_crystal[3]), lambda_="neyman"))
    plt.plot(x, crystalball(x, *best_crystal)+line(x, 50, 0.5), 'r-', label='mean = {}, sigma = {}'.format(best_crystal[2], best_crystal[3]))
    plt.plot(x, expo(x, 14.3, -3.15), 'g-')
    plt.xlabel('Massa Invariante [GeV]')
    plt.ylabel('Número de Eventos')
    plt.title('J/Psi: Ajuste com CrystalBall')
    plt.legend()
    plt.show()
