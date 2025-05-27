foundSolutions = []

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        first = 0
        second = 1
        foundSolutions.extend([first, second])
        for i in range(2, n+1):
            newSolution = foundSolutions[i-1] + foundSolutions[i-2]
            foundSolutions.append(newSolution)
        return newSolution
    
num = fibonnaci(5)
print(num)
for j in range(len(foundSolutions)):
    print(foundSolutions[j])