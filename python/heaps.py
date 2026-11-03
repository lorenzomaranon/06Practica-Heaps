import heapq


def top_k(datos, k):
    mejores = []
    
    if k < 0:
        raise ValueError("k no puede ser negativo")
    if k == 0: 
        return []

    
    for i in datos:
        if len(mejores) < k:
            heapq.heappush(mejores, i)
        elif i > mejores[0]:
            heapq.heapreplace(mejores,i)        

    mejores.sort(reverse=True)
    return mejores