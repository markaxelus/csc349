import math
import numpy as np
import matplotlib.pyplot as plt

# compute the Euler-based numerical approximation
# to the falling parachutist problem
#
# return the result as a np.array with two columns
# the first one containing the times in seconds
# and the second the values of the approximation

def skyfall_euler(m,c,g,t0,v0,tn,n):
  # computer step size h
  h = (tn-t0)/n
  # set t, v to initial values
  t = t0
  v = v0

  # allocate array for result
  result = np.zeros((n+1,2))
  result[0] = [t,v]
  # compute v(t) over n time steps using Euler’s method
  for i in range(1,n+1):
    v=v+(g-c/m*v)*h
    t=t+h
    result[i,:] = [t,v]
  return result

# print the returned values
def output_values(result):
  print('value of t approximation v(t)\n')
  for r in result:
    t,v = r
    print(f"{t:8.3f} {v:19.4f}")

# Your code goes here
result_1a = skyfall_euler(68.1, 12.5, 9.81, 0, 0, 12, 6)

# Your code goes here
result_1b = skyfall_euler(62.8, 12.5, 9.81, 0, 0, 12, 15)


# Your code goes here
result_1c = skyfall_euler(62.8, 12.5, 3.71, 0, 0, 12, 15)

def skyfall_analytic(g,m,c,t):
  # modify code as described above to return the right value
  return ((g*m)/c) * (1 - math.exp(-c*t/m))

def relative_error(exact, approximate):
  # modify code as described above to return the right value
  return abs(exact - approximate) / abs(exact)


def skyfall_numeric(g,m,c,t):
  # modify code as described above to return the right value
  skyfall_e = skyfall_euler(m, c, g, 0, 0, t, 15)
  return skyfall_e[-1,1]

# this code will display the relative error once the functions are
# implemented correctly
p = skyfall_analytic (9.81,62.8,12.5,12)
pstar = skyfall_numeric(9.81,62.8,12.5,12)

e_a = relative_error(p, pstar)
print(f"Relative Error: {e_a:8.4f}")



def skyfall_euler2(m,k,g,t0,v0,tn,n):
  # modify code as described above to return the right array of times and values
  # computer step size h
  h = (tn-t0)/n
  # set t, v to initial values
  t = t0
  v = v0

  # allocate array for result
  result = np.zeros((n+1,2))
  result[0] = [t,v]
  # compute v(t) over n time steps using Euler’s method
  for i in range(1,n+1):
    v=v+(g-k/m*v**2)*h
    t=t+h
    result[i,:] = [t,v]
  return result

result_2a = skyfall_euler2(73.5,0.234,9.81,0,0,18,72)
output_values(result_2a)

def skyfall_analytic2(g,m,k,t):
  # modify code as described above to return the right value
  # v(t) = sqrt(gm/k) * tanh(sqrt(gk/m) * t)
  return math.sqrt(g*m/k) * math.tanh(math.sqrt(g*k/m) * t)

def skyfall_numeric2(g,m,k,t):
  # modify code as described above to return the right value
  skyfall_e2 = skyfall_euler2(m, k, g, 0, 0, t, 72)
  return skyfall_e2[-1,1]


p =  skyfall_analytic2(9.81, 73.5, 0.234, 18)
pstar = skyfall_numeric2(9.81, 73.5, 0.234, 18)
e_a = relative_error(p, pstar)

relative_error_scientific = f"{e_a:e}"  # Using f-string
print(relative_error_scientific)


# enegx_Taylor1 Approximates e^(-x) with the
# nth degree McLaurin polynomial for e^(-x)

def enegx_Taylor1(x,n):
  # modify code as described above to return the right value
  result = 0
  for i in range(n+1):
    term = ((-1)**i) * (x**i) / math.factorial(i)
    result += term
  return result

# enegx_Taylor2 Approximates e^(-x) with 1 over
# the nth degree McLaurin polynomial for e^x

def enegx_Taylor2(x,n):
  # modify code as described above to return the right value
  denominator = 0
  for i in range(n+1):
    term = (x ** i) / math.factorial(i)
    denominator += term
  return 1 / denominator

approximations1 = np.array([enegx_Taylor1(2.0, n) for n in range(1, 6)])
approximations2 = np.array([enegx_Taylor2(2.0, n) for n in range(1, 6)])
exact = np.full(5, np.exp(-2.0))

print(exact)
print(approximations1)
print(approximations2)

relative_error1 = np.abs(exact - approximations1) / np.abs(exact)
relative_error2 = np.abs(exact - approximations2) / np.abs(exact)

print(relative_error1)
print(relative_error2)


# your code goes here
fig, ax = plt.subplots()
exact_values = np.full(5, exact)

plt.plot(approximations1, 'b-', label="Approximation1 (Direct McLaurin)")
plt.plot(approximations2, color="orange", linestyle='-', label="Approximation2 (Reciprocal)")
plt.plot(exact_values, 'g-', label="Exact")
# Add labels and title
plt.xlabel("Order of polynomial approximation")
plt.ylabel("Approximate value of function")

# change title appropriately
plt.title("Approximations of e^(-2.0) with Taylor Series")

plt.legend()
# save the plot to a file
plt.savefig("csc349a_asn1_q3.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()


# set the best approximation to either "Approximation 1" or "Approximation 2"
# depending on which one you consider best
best_approximation = "Approximation 2"



