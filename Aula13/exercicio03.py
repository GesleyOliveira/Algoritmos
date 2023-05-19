def numerotriangular(n):
    for i in range(3,n+1):
        if (i-2)*(i-1)*(i)==n:
            return True
    return False

# Segunda versão usando laço while

def numeroTriangular2(n):
    i=3
    while i<n:
        if (i-2)*(i-1)*(i)==n:
            return True
        i=i+1
    return False



