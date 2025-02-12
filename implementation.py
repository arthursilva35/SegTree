from array import array


# implementacao simples de uma segment tree de soma
a = [1, 3, -2, 8, -7]
st = [0] * (4*len(a)) # tamanho da arvore é O(4n) -> 1 + 2 + 4 ... 2^logn <= 2^logn + 1 <= 4n

# algoritmo recursivo para construcao da arvore
# v: idx do vertice # l: limite esquerdo do intervalo do vertice # r: limite direito do intervalo do vertice 
def constroi(a: list, v: int, l: int, r: int) -> None:  
    
    global st

    if( l == r ):
        st[v] = a[l] # nós folhas (caso base)
        return None
    else:
        m = (l + r)/2

        m = int(m)

        print(l, m, r)
        constroi(a, v*2, l, m)
        constroi(a, v*2+1, m + 1, r)
        st[v] = st[v*2] + st[v*2 + 1] # a soma de um vértice interno e soma da soma dos seus filhos
        return None
    

constroi(a, 1, 0, 4)
print(st)