class Myclass(object):
      def __init__(self, value, table):
          self.value = value
          self.table = table


def knapsack(W, val, wgh, n):
    K = [[Myclass(0,[False for x in range(n)]) for x in range(W+1)] for y in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                 K[i][w].value = 0
                 K[i][w].table = [False for x in range(n)]
            elif wgh[i-1] > w:
                K[i][w] = K[i-1][w]
            else:
                if val[i-1] + K[i-1][w-wgh[i-1]].value > K[i-1][w].value:
                    K[i][w].value = val[i-1] + K[i-1][w-wgh[i-1]].value
                    K[i][w].table = K[i-1][w-wgh[i-1]].table
                    K[i][w].table[i-1] = True
                else:
                    K[i][w] = K[i-1][w]
    return K[n][W]

val = [60, 100, 120]
wgh = [10, 20, 30]
W = 50
n = len(val)
result = knapsack(W, val, wgh, n)
print(result.value)
print(result.table)






























































