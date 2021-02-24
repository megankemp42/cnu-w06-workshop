import numpy as np
import matplotlib.pyplot as plt

def monte_carlo(f, a, b, N):
    xi = (b-a)*np.random.random_sample(N,)+a
    y = f(xi)
    avg = 0
    for j in y:
        avg += j
    avg = avg/N
    return (b-a)*avg

def f(x):
    return x**2

testNs = [1, 2, 4, 8, 16, 30, 50, 80, 100, 200, 400, 600, 800, 1000]

estimates = []
errors = []
qs = []

for N in testNs:
    est = monte_carlo(f, 1, 4, N)
    estimates.append(est)
    errors.append(est - 21)

for k in range(len(errors)):
    qs.append(np.log(errors[k])/np.log(testNs[k]))

print(errors)
print(qs)