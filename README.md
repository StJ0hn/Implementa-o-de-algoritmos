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
## Djikstra (Caminho mínimo)
```
import heapq
import math

def dijkstra(grafo, vertice_inicial):
    distancias = {vertice: math.inf for vertice in grafo}
    distancias[vertice_inicial] = 0
    predecessores = {vertice: None for vertice in grafo}
    fila_prioridade = [(0, vertice_inicial)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso_aresta in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso_aresta

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return distancias, predecessores

# --- Execução ---

meu_grafo = {
    'S': {'A': 7, 'B': 2, 'C': 3},
    'A': {'S': 7, 'B': 3, 'D': 4},
    'B': {'S': 2, 'A': 3, 'D': 4, 'C': 1},
    'C': {'S': 3, 'B': 1, 'E': 2},
    'D': {'A': 4, 'B': 4, 'E': 2},
    'E': {'C': 2, 'D': 2}
}

origem = 'S'
distancias_finais, predecessores_finais = dijkstra(meu_grafo, origem)

# --- Impressão dos Resultados ---
print(f"Executando Dijkstra a partir da origem: {origem}\n")
print(f"{'Vértice':<12} | {'Distância Mínima':<18} | {'Predecessor':<12}")
print("-" * 50)

for vertice in sorted(distancias_finais):
    dist = distancias_finais[vertice]
    pred = predecessores_finais[vertice] or 'N/A'
    print(f"{vertice:<12} | {dist:<18} | {pred:<12}")
```
