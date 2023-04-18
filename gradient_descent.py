

def descent(x,real_y,curr_a, curr_b):
    lr = 0.000001
    new_a = curr_a - lr * (curr_a * x + curr_b - real_y) * x
    new_b = curr_b - lr * (curr_a * x + curr_b - real_y)
    return new_a, new_b


def train_model(x, y):
    a = 1
    b = 0
    for i in range(100000):
        a, b = descent(x, y, a, b)

    return a, b


def test_descent(a,b,x,y):
    print("X:", x)
    print("Real y:", y)
    print("Predicted Y:", a*x + b)
    print("Absolute error:", y - (a*x + b))
    print("Relative error:", abs((y - (a*x + b)) / y))


x = 15.1
y = 4.7

a, b = train_model(x, y)
test_descent(a, b, x, y)
