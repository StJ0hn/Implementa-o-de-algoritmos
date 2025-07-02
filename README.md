# Implementação de algoritmos 
- Esse repositório consiste na implementação dos algoritmos explorados na matéria de **Algoritmos em Grafos**
- Abordando os seguintes algoritmos:
## DFS (Busca em Profundidade):
```
DFS(G)
1  para cada vértice u ∈ V[G]
2      u.cor = BRANCO
3      u.π = NIL
4. tempo = 0
5. para cada vértice u ∈ V[G]
6      se u.cor == BRANCO
7          DFS-VISIT(G, u)

DFS-VISIT(G, u)
1. tempo = tempo + 1      // vértice branco acabou de ser descoberto
2. u.d = tempo
3. u.cor = CINZENTO
4. para cada v ∈ G.Adj[u] // explorar aresta (u, v)
5.     se v.cor == BRANCO
6.         v.π = u
7.         DFS-VISIT(G, v)
8. u.cor = PRETO          // pintar u de preto; está terminado
9. tempo = tempo + 1
```
