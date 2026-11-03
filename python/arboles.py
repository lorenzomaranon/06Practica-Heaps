

class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


def espejo(raiz: Nodo):
    if raiz is None:
        return None
    
    return Nodo(raiz.valor, espejo(raiz.der), espejo(raiz.izq))


def son_espejo(a: Nodo, b: Nodo):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False

    return (a.valor == b.valor and 
            son_espejo(a.izq,b.der) and 
            son_espejo(a.der, b.izq))

def es_simetrico(raiz):
    if raiz is None:
        return True
    return son_espejo(raiz.izq, raiz.der)

def inorden(raiz):
    salida = []
    def visitar(nodo):
        if nodo is not None:
            visitar(nodo.izq)
            salida.append(nodo.valor)
            visitar(nodo.der)
    visitar(raiz)
    return salida
