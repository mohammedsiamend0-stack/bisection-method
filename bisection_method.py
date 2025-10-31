
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Define the function f(x) = x³ - 4x - 9
    """
    return x**3 - 4*x - 9

def bisection_method(a, b, tolerance=0.0001, max_iterations=100):
    """
    Bisection Method Implementation

    Parameters:
    a: Lower bound of interval
    b: Upper bound of interval
    tolerance: Acceptable error tolerance
    max_iterations: Maximum number of iterations

    Returns:
    root: Approximate root
    iterations: List of iteration details
    """

    # Check if initial guesses bracket a root
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs")
        return None, None

    iterations = []
    iteration = 0

    print(f"{'Iter':<6} {'a':<12} {'b':<12} {'c':<12} {'f(a)':<12} {'f(b)':<12} {'f(c)':<12} {'Error %':<12}")
    print("-" * 90)

    while iteration < max_iterations:
        # Calculate midpoint
        c = (a + b) / 2

        # Calculate function values
        fa = f(a)
        fb = f(b)
        fc = f(c)

        # Calculate error
        if iteration > 0:
            error = abs((c - iterations[-1]['c']) / c) * 100
        else:
            error = 100

        # Store iteration data
        iter_data = {
            'iteration': iteration + 1,
            'a': a,
            'b': b,
            'c': c,
            'fa': fa,
            'fb': fb,
            'fc': fc,
            'error': error
        }
        iterations.append(iter_data)

        # Print iteration details
        print(f"{iteration+1:<6} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fa:<12.6f} {fb:<12.6f} {fc:<12.6f} {error:<12.6f}")

        # Check for convergence
        if abs(fc) < tolerance or error < tolerance:
            print(f"\nRoot found: {c:.6f}")
            print(f"Function value at root: {fc:.6f}")
            print(f"Number of iterations: {iteration + 1}")
            return c, iterations

        # Update interval
        if fa * fc < 0:
            b = c
        else:
            a = c

        iteration += 1

    print(f"\nMaximum iterations reached. Approximate root: {c:.6f}")
    return c, iterations

def plot_function(a, b, root=None):
    """
    Plot the function and mark the root
    """
    x = np.linspace(a - 1, b + 1, 1000)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x) = x³ - 4x - 9')
    plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    plt.grid(True, alpha=0.3)

    if root is not None:
        plt.plot(root, f(root), 'ro', markersize=10, label=f'Root ≈ {root:.6f}')

    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title('Bisection Method - Function Plot', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_convergence(iterations):
    """
    Plot the convergence of the method
    """
    iter_nums = [iter_data['iteration'] for iter_data in iterations]
    errors = [iter_data['error'] for iter_data in iterations]

    plt.figure(figsize=(10, 6))
    plt.semilogy(iter_nums, errors, 'b-o', linewidth=2, markersize=6)
    plt.xlabel('Iteration Number', fontsize=12)
    plt.ylabel('Relative Error (%)', fontsize=12)
    plt.title('Convergence of Bisection Method', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    print("=" * 90)
    print("BISECTION METHOD FOR ROOT FINDING")
    print("Equation: f(x) = x³ - 4x - 9")
    print("=" * 90)
    print()

    # Initial interval [a, b]
    a = 2.0
    b = 3.0

    print(f"Initial interval: [{a}, {b}]")
    print(f"f({a}) = {f(a):.6f}")
    print(f"f({b}) = {f(b):.6f}")
    print()

    # Apply bisection method
    root, iterations = bisection_method(a, b, tolerance=0.0001)

    if root is not None:
        print()
        print("=" * 90)

        # Plot the function and root
        plot_function(a, b, root)

        # Plot convergence
        plot_convergence(iterations)
