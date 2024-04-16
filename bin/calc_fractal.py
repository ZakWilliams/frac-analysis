#!/usr/bin/env python

from numpy import angle, linspace, newaxis, pi, savetxt

import argparse

def newton(function, derivative, initial_estimate, num_iters=10):
    '''Solves the equation `function`(x) == 0 using the Newton&ndash;Raphson
    method with `num_iters` iterations, starting from `initial_estimate`.
    `derivative` is the derivative of `function` with respect to x.'''

    current_estimate = initial_estimate
    for _ in range(num_iters):
        current_estimate = (
            current_estimate
            - function(current_estimate) / derivative(current_estimate)
        )
    return current_estimate


def complex_linspace(lower, upper, num_real, num_imag):
    real_space = linspace(lower.real, upper.real, num_real)
    imag_space = linspace(lower.imag, upper.imag, num_imag) * 1J
    return real_space + imag_space[:, newaxis]

def polynomial(x):
    return x ** 3 - 1
    # return x ** 5 - 1
    # return x ** 6 - 1

def derivative(x):
    return 3 * x ** 2
    # return 5 * x ** 4
    # return 6 * x ** 5


parser = argparse.ArgumentParser()
parser.add_argument('order', type=int, help="Order of the polynomial")
parser.add_argument('outfile', type=str, help="Where to put the output file")
args = parser.parse_args()

if args.order == 3:
    def polynomial(x):
        return x ** 3 - 1

    def derivative(x):
        return 3 * x ** 2
elif args.order == 5:
    def polynomial(x):
        return x ** 5 - 1

    def derivative(x):
        return 5 * x ** 4
elif args.order == 6:
    def polynomial(x):
        return x ** 6 - 1

    def derivative(x):
        return 6 * x ** 5
else:
    raise ValueError(f"I don't know how to handle order {args.order}.")




z_min = -1 - 1J
z_max = 1 + 1J
initial_z = complex_linspace(z_min, z_max, 1000, 1000)

results = angle(newton(polynomial, derivative, initial_z, 20))
savetxt("results/data.dat", results)
