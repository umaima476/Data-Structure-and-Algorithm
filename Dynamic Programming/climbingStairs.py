def countWays(n):
    solved = [0] * (n+1)
    if n == 0 or n == 1:
        return 1
    elif n >= 2:
        solved[0], solved[1] = 1, 1
        for i in range(2, n+1):
            solved[i] = solved[i-1] + solved[i-2]
    return solved[n]
    
n = 5
ways = countWays(5)
print(f"Stairs of steps {n} can be climed in {ways} number of ways")