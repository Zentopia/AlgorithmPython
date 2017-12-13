capacity = 7
num = 4

optimal_matrix = [[0 for x in range(capacity + 1)] for y in range(num + 1)]
weight = [0, 1, 3, 4, 5]
value = [0, 1, 4, 5, 7]

for c in range(capacity + 1):
    for n in range(1, num + 1):
        if weight[n] <= c:
            print("c:", c, "n:", n)
            optimal_matrix[n][c] = max(value[n]+ optimal_matrix[n - 1][c - weight[n]], optimal_matrix[n - 1][c])
        else:
            optimal_matrix[n][c] = optimal_matrix[n - 1][c]

print("max_value: ", optimal_matrix[num][capacity])

c = capacity
n = num

while n > 0:
    if optimal_matrix[n][c] == optimal_matrix[n - 1][c]:
        n = n - 1
    else:
        print("index:", n, "weight:", weight[n], "value:", value[n])
        c = c - weight[n]
        n = n - 1

"""宝宝写的
num = 4
capacity = 7
value = [0,1,4,5,7]
weight = [0,1,3,4,5]
result = [[0 for i in range(capacity+1)] for y in range(num+1)]
for n in range(num+1):
    for c in range(1, capacity+1):
        if weight[n]<= c:
            print("n:",n,"c:",c)
            result[n][c] = max(value[n] + result[n - 1][c - weight[n]], result[n - 1][c])
            print("result:",result[n][c],  result[n - 1][c - weight[n]], "index", c - weight[n])
            pass
        else:
            result[n][c] = result[n - 1][c]
print(result)
"""
