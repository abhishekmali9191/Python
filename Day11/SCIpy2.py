from scipy.integrate import quad
#define the integrand
def integrand(x):
    return x**2
#compute the integral -(curve of x2)
result,error = quad(integrand,0,1)
print(result)   #integral result

# #####################################
# OUTPUT
# 0.33333333333333337