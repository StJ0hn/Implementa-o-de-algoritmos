import heapq
import math

def dijkstra(grafo, vertice_inicial):
    """
    Implementação do Algoritmo de Dijkstra usando uma fila de prioridade (min-heap).

    Args:
        grafo (dict): O grafo representado como uma lista de adjacência.
                      Formato: {'vertice': {'vizinho1': peso1, 'vizinho2': peso2}}
        vertice_inicial (str): O vértice de onde a busca começará.

    Returns:
        tuple: Uma tupla contendo dois dicionários (distancias, predecessores).
    """

    # 1. Inicialização
    # Dicionário para armazenar as distâncias mínimas da origem até cada vértice.
    # Começa com infinito para todos, exceto para a origem, que é 0.
    distancias = {vertice: math.inf for vertice in grafo}
    distancias[vertice_inicial] = 0

    # Dicionário para reconstruir os caminhos.
    predecessores = {vertice: None for vertice in grafo}

    # Fila de prioridade para determinar o próximo vértice a visitar.
    # Armazena tuplas de (distancia, vertice).
    # O heapq sempre manterá a tupla com a menor distância no topo.
    fila_prioridade = [(0, vertice_inicial)]

    # 2. Laço Principal do Algoritmo
    # Continua enquanto houver vértices na fronteira para serem explorados.
    while fila_prioridade:

        # 3. ESCOLHER o vértice não visitado com a menor distância.
        # heapq.heappop() remove e retorna o item com a menor prioridade (distância).
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # Otimização: se já encontramos um caminho mais curto para este vértice, ignoramos.
        if distancia_atual > distancias[vertice_atual]:
            continue

        # 4. ATUALIZAR OS VIZINHOS do vértice escolhido.
        # Para cada vizinho, verificamos se um caminho mais curto foi encontrado.
        for vizinho, peso_aresta in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso_aresta

            # Se o novo caminho (passando pelo vertice_atual) for mais curto...
            if nova_distancia < distancias[vizinho]:
                # ...atualizamos a distância e o predecessor.
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = vertice_atual
                # E adicionamos o vizinho à fila para ser explorado futuramente.
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    # 5. Retornar os resultados finais.
    return distancias, predecessores

# --- Execução com o nosso grafo de exemplo ---

# Representação do grafo ponderado do exercício
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
    pred = predecessores_finais[vertice] or 'N/A' # Trata o 'None' da origem
    print(f"{vertice:<12} | {dist:<18} | {pred:<12}")
