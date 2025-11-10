# PathFinder - Algoritmo A* para Labirinto 2D

## 📋 Descrição do Projeto

Este projeto implementa o **Algoritmo A*** para resolver o problema de busca de caminho em um labirinto 2D. O objetivo é encontrar o menor caminho entre um ponto inicial (S) e um ponto final (E), evitando obstáculos e navegando apenas por células livres.

O algoritmo foi desenvolvido como parte do trabalho da disciplina de **Fundamentos de Projeto e Análise de Algoritmos (FPAA)** do cursod de Engenharia de Software da PUC Minas.

### Contexto

Um robô de resgate precisa navegar por um labirinto para chegar ao seu destino pelo caminho mais curto possível. O labirinto é representado por uma matriz 2D onde:
- `S` - Ponto inicial (Start)
- `E` - Ponto final (End)
- `0` - Célula livre (o robô pode passar)
- `1` - Obstáculo (o robô não pode passar)

O robô pode se mover para células adjacentes (cima, baixo, esquerda, direita), desde que não sejam obstáculos ou estejam fora dos limites do labirinto. Cada movimento tem custo igual a 1.

---

## 🎯 Algoritmo A* (A-Star)

O **Algoritmo A*** é um algoritmo de busca de caminho que combina características do algoritmo de Dijkstra e da busca gulosa (greedy). Ele é amplamente utilizado em inteligência artificial, jogos e robótica devido à sua eficiência.

### Como funciona?

O A* utiliza uma **função de avaliação** para cada nó:

```
f(n) = g(n) + h(n)
```

Onde:
- **g(n)**: Custo real do caminho do início até o nó atual
- **h(n)**: Heurística - estimativa do custo do nó atual até o destino
- **f(n)**: Custo total estimado do caminho passando por este nó

### Heurística de Manhattan

Neste projeto, utilizamos a **Distância de Manhattan** como função heurística:

```
h(n) = |x_atual - x_final| + |y_atual - y_final|
```

Esta heurística é **admissível** (nunca superestima o custo real) e **consistente**, garantindo que o A* encontre o caminho ótimo.

### Passos do Algoritmo

1. **Inicialização**: Criar o nó inicial com g=0 e calcular h e f
2. **Lista Aberta**: Manter uma fila de prioridade com nós a explorar (ordenados por f)
3. **Lista Fechada**: Manter conjunto de nós já explorados
4. **Exploração**:
   - Pegar o nó com menor f da lista aberta
   - Se é o destino, reconstruir e retornar o caminho
   - Senão, explorar seus vizinhos válidos
   - Para cada vizinho:
     - Calcular g, h e f
     - Se não foi explorado ou encontrou caminho melhor, adicionar à lista aberta
5. **Fim**: Se lista aberta esvaziar sem encontrar destino, não há solução

### Complexidade

- **Tempo**: O(b^d) no pior caso, onde b é o fator de ramificação e d é a profundidade da solução
- **Espaço**: O(b^d) para armazenar todos os nós gerados
- Na prática, com uma boa heurística, o A* é muito mais eficiente que busca em largura ou profundidade

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.6 ou superior instalado
- Bibliotecas padrão do Python (não requer instalação adicional)

### Execução

1. Clone ou baixe o repositório:
```bash
git clone https://github.com/mateusfaissal/PathFinder-FPAA.git
cd PathFinder
```

2. Execute o programa:
```bash
python3 pathfinder.py
```

O programa executará três exemplos demonstrativos:
- Exemplo 1: Labirinto do PDF (com solução)
- Exemplo 2: Labirinto sem solução
- Exemplo 3: Labirinto maior

---

## 📝 Exemplos de Uso

### Exemplo 1: Labirinto do PDF

**Entrada:**
```
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
```

**Saída:**
```
Menor caminho encontrado com 7 passos!
Coordenadas: [s(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), e(3, 3)]

Labirinto com caminho destacado:
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```

### Exemplo 2: Labirinto Sem Solução

**Entrada:**
```
S 0 1 0 0
0 0 1 0 1
1 1 1 1 1
1 0 0 E 1
```

**Saída:**
```
Sem solução - não há caminho possível entre S e E.
```

### Exemplo 3: Labirinto Maior

**Entrada:**
```
S 0 0 0 1 0 0
1 1 0 0 1 0 0
0 0 0 1 1 0 1
0 1 0 0 0 0 0
0 1 1 1 0 1 0
0 0 0 0 0 1 E
```

**Saída:**
```
Menor caminho encontrado com 12 passos!
Coordenadas: [s(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 6), e(5, 6)]

Labirinto com caminho destacado:
S * * 0 1 0 0
1 1 * 0 1 0 0
0 0 * 1 1 0 1
0 1 * * * * *
0 1 1 1 0 1 *
0 0 0 0 0 1 E
```

---

...
