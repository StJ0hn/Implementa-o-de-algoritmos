#Criando o grafo usando uma lista de adjacência
meu_grafo = {'A': ['B', 'C'],
'B': ['E'],
'C': ['D', 'F'],
'D': ['B'],
'E': ['A'],
'F': ['F']}

def dfs(meu_grafo):
    # Dicionários de estado criados aqui
    cor = {}
    pi = {}
    tempo_d = {}
    tempo_f = {}
    tempo = [0]

    #laço de inicialização
    for vertice in meu_grafo:
        cor[vertice] = 'BRANCO'
        pi[vertice] = None

    #laço principal de busca
    for vertice in meu_grafo:
        if cor[vertice] == 'BRANCO':
            dfs_visit(vertice, meu_grafo, cor, pi, tempo_d, tempo_f, tempo)
    return tempo_d, tempo_f, pi



def dfs_visit(u, meu_grafo, cor, pi, tempo_d, tempo_f, tempo):
    cor[u] = 'CINZENTO'
    tempo[0] += 1
    tempo_d[u] = tempo[0]
    for v in meu_grafo[u]:
        if cor[v] == 'BRANCO':
            pi[v] = u;
            dfs_visit(v, meu_grafo, cor, pi, tempo_d, tempo_f, tempo)
    cor[u] = 'PRETO'
    tempo[0] += 1
    tempo_f[u] = tempo[0]


pi_final, d_final, f_final = dfs(meu_grafo)
print("--- DADOS BRUTOS DA BUSCA ---")

print("\nDicionário de Predecessores (pi):")
print(pi_final)

print("\nDicionário de Tempo de Descoberta (d):")
print(d_final)

print("\nDicionário de Tempo de Finalização (f):")
print(f_final)
