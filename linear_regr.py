def regr(x):
    ages = [12, 13, 16, 19, 13, 14, 17, 18, 14, 16]
    weights = [50, 55, 48, 58, 59, 55, 49, 52, 42, 56]
    m = gradient(ages, weights)
    c = intercept(ages, weights, m)
    y_pred = (m * x) + c
    return round(y_pred, 2)

def gradient(X, Y):
    # Compute coefficient m's
    x_mean = mean(X)
    y_mean = mean(Y)
    # compute the difference between x and x_mean, y and y_mean
    x_dev = deviation(X, x_mean)
    y_dev = deviation(Y, y_mean)
    xy_dev = []
    x_dev_square = []
    if len(x_dev) != len(y_dev):
        raise ValueError("The lengths of x_dev and y_dev must be the same")
    for i in range(len(x_dev)):
        xDev_dot_yDev = x_dev[i] * y_dev[i]
        xy_dev.append(xDev_dot_yDev)
        x_dev_square.append(x_dev[i]**2)
    sum_xy_dev = sum(xy_dev)
    sum_x_dev_square = sum(x_dev_square)

    if sum_x_dev_square == 0:
        raise ValueError("Zero division is not allowed")

    return sum_xy_dev / sum_x_dev_square

def intercept(X, Y, slope):
    x_mean = mean(X)
    y_mean = mean(Y)
    return y_mean - (x_mean * slope)

def deviation(A, b):
    dev = []
    for a in A:
        dev.append(a - b)
    return dev

def mean(args):
    if len(args) < 1:
        raise ValueError("List length cannot zero (0)")
    # compute fx of the individual entry
    args_fx = [x * args.count(x) for x in set(args)]
    # frequency of the data
    args_length = len(args)
    args_mean = sum(args_fx) / args_length
    return args_mean

try:
    age = int(input("Please, enter your age here for weight prediction: "))
except ValueError as e:
    print("Invalid value entered")
else:
    print(regr(age))