import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ds = pd.read_csv('DoubleMuRun2011A.csv')
print(ds.head())

invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2) ))
print('The first five values calculated (in units GeV):')
print(invariant_mass[0:5])

# Let's limit the fit near to the peak of the histogram.
lowerlimit = eval(input('Insira o limite mais baixo do fit: '))
upperlimit = eval(input('Insira o limite mais alto do fit: '))
bins = eval(input('Insira a binagem desejada: '))

# Let's select the invariant mass values that are inside the limitations.
limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

#Let's create a histogram of the selected values.
histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))

# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
y = histogram[0]
x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )

# Let's define a function that describes Breit-Wigner distribution for the fit.
# E is the energy, gamma is the decay width, M the maximum of the distribution
# and a, b and A different parameters that are used for noticing the effect of
# the background events for the fit.
def breitwigner(E, gamma, M, a, b, A):
    return a*E+b+A*( (2*np.sqrt(2)*M*gamma*np.sqrt(M**2*(M**2+gamma**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gamma**2)))) )/((E**2-M**2)**2+M**2*gamma**2)

def gaussian(x, a, x0, sigma = np.sqrt(sum(y*(x - (sum(x * y) / sum(y)))**2))):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

# Initial values for the optimization in the following order:
# gamma (the full width at half maximum (FWHM) of the distribution)
# M (the maximum of the distribution)
# a (the slope that is used for noticing the effect of the background)
# b (the y intercept that is used for noticing the effect of the background)
# A (the "height" of the Breit-Wigner distribution)

initials_breit = 0
initials_gauss = 0 
choice = 0
while(choice>2 or choice<1):
    choice = eval(input("Escolha 1 ou 2: Enter 1> Breit-Wigner ou Enter 2> Gaussian: "))
    choice = int(choice)
    if choice == 1:
        initials_breit =  [float(x) for x in input('Preencha com os parâmetros da Briet-Wigner (gamma, M, a, b e A) dando apenas espaços entre eles: ').split()] #Para o Z:[4, 91, -2, 150, 13000] Para o Upsilon: [0.5 9.5 20 -80 200]
        # Let's import the module that is used in the optimization, run the optimization
        # and calculate the uncertainties of the optimized parameters.
        best_breit, covariance = curve_fit(breitwigner, x, y, p0=initials_breit, sigma=np.sqrt(y))
        error_breit = np.sqrt(np.diag(covariance))
    
        # Let's print the values and uncertainties that are got from the optimization.
        print("The values and the uncertainties from the optimization")
        print("")
        first = "The value of the decay width (gamma) = {} +- {}".format(best_breit[0], error_breit[0])
        second = "The value of the maximum of the distribution (M) = {} +- {}".format(best_breit[1], error_breit[1])
        third = "a = {} +- {}".format(best_breit[2], error_breit[2])
        fourth = "b = {} +- {}".format(best_breit[3], error_breit[3])
        fifth = "A = {} +- {}".format(best_breit[4], error_breit[4])
        print(first)
        print(second)
        print(third)
        print(fourth)
        print(fifth)

        plt.plot(x, breitwigner(x, *best_breit), 'r-', label='gamma = {}, M = {}'.format(best_breit[0], best_breit[1]))
        plt.xlabel('Invariant mass [GeV]')
        plt.ylabel('Number of event')
        plt.title('The Breit-Wigner fit')
        plt.legend()
        plt.show()
    else:
        initials_gauss =  [float(x) for x in input('Preencha com os parâmetros da Gauss (max(y), mean, sigma): ').split()] 
        # Let's import the module that is used in the optimization, run the optimization
        # and calculate the uncertainties of the optimized parameters.
        best_gauss, covariance = curve_fit(gaussian, x, y, p0=initials_gauss, sigma=np.sqrt(y))
        error_gauss = np.sqrt(np.diag(covariance))
    
        # Let's print the values and uncertainties that are got from the optimization.
        print("The values and the uncertainties from the optimization")
        print("")
        first = "The value of max(y
) = {} +- {}".format(best_gauss[0], error_gauss[0])
        second = "The value of mean = {} +- {}".format(best_gauss[1], error_gauss[1])
        third = "The value of sigma = {} +- {}".format(best_gauss[2], error_gauss[2])
        print(first)
        print(second)
        print(third)

        plt.plot(x, gaussian(x, *best_gauss), 'r-', label='x = {}, x0 = {}'.format(best_gauss[0], best_gauss[1]))
        plt.xlabel('Invariant mass [GeV]')
        plt.ylabel('Number of event')
        plt.title('The Gaussian fit')
        plt.legend()
        plt.show()


