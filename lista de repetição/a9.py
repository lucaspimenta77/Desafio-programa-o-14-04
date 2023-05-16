for x in range(10, 51):
    x /= 10.0
    y = (3 + 2*x + 6*x**2) / (1 + 9*x + 16*x**2)
    print("x =", x, "| y =", y)
