def max_expression_value(arr):
    # Initialize the maximum value as negative infinity
    max_value = float("-inf")
    count = 0
    # Iterate through all possible combinations of u, v, w, x
    for u in range(len(arr)):
        for v in range(u):
            for w in range(v):
                for x in range(w):
                    # Calculate the value of the expression for the current combination
                    expression_value = arr[u] - arr[v] + arr[w] - arr[x]

                    # Update the maximum value if the current value is greater
                    if expression_value > max_value:
                        max_value = expression_value
    return max_value


a = [3, 9, 10, 1, 30, 40]
print(a)
print(max_expression_value(a))

b = [2, 56, 22, 89, 10, 64, 14, 97, 30]
print(b)
print(max_expression_value(b))