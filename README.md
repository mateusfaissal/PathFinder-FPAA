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

## 💻 Uso Programático

### Criando seu próprio labirinto

```python
from pathfinder import PathFinder

# Definir o labirinto
maze = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 'E', 1]
]

# Criar o PathFinder
pathfinder = PathFinder(maze)

# Exibir labirinto original
pathfinder.display_path()

# Encontrar o caminho
path = pathfinder.find_path()

if path:
    print(f"\nMenor caminho: {pathfinder.format_path_output(path)}")
    pathfinder.display_path(path)
else:
    print("\nSem solução")
```

---

## 🏗️ Estrutura do Código

### Classe `Node`
Representa um nó no grafo de busca:
- `position`: coordenadas (linha, coluna)
- `parent`: referência ao nó pai
- `g`: custo do início até este nó
- `h`: heurística (Manhattan) até o destino
- `f`: custo total (g + h)

### Classe `PathFinder`
Implementa o algoritmo A*:
- `__init__(maze)`: inicializa com o labirinto
- `heuristic(pos1, pos2)`: calcula distância de Manhattan
- `get_neighbors(position)`: retorna vizinhos válidos
- `find_path()`: executa o algoritmo A*
- `display_path(path)`: visualiza o labirinto com caminho
- `format_path_output(path)`: formata saída do caminho

---

## ✅ Requisitos Implementados

- ✅ Leitura de labirinto como matriz 2D
- ✅ Validação de existência de S e E
- ✅ Implementação da heurística de Manhattan
- ✅ Implementação completa do Algoritmo A*
- ✅ Exibição do caminho em coordenadas
- ✅ Visualização do caminho no labirinto
- ✅ Tratamento de casos sem solução
- ✅ Documentação completa no README.md
- ✅ Múltiplos exemplos de teste

---

## 🎓 Conceitos de FPAA Aplicados

### Estruturas de Dados
- **Fila de Prioridade (Heap)**: para lista aberta, garantindo O(log n) nas operações
- **Conjunto (Set)**: para lista fechada, garantindo O(1) nas verificações
- **Dicionário (Dict)**: para rastrear melhor custo g de cada posição

### Algoritmos de Busca
- **Busca Informada**: uso de heurística para guiar a exploração
- **Busca Ótima**: garantia de encontrar o caminho mais curto
- **Backtracking**: reconstrução do caminho através dos nós pais

### Análise de Complexidade
- **Complexidade de Tempo**: O(b^d) onde b é o fator de ramificação médio
- **Complexidade de Espaço**: O(b^d) para armazenar nós explorados
- **Otimalidade**: garantida quando heurística é admissível e consistente

---

## 👥 Autores

- Arthur Curi Kramberger
- Helio Ernesto
- Lucas Cerqueira
- Mateus Faissal

---

## 📚 Referências

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). *A Formal Basis for the Heuristic Determination of Minimum Cost Paths*
- Cormen, T. H., et al. (2009). *Introduction to Algorithms* (3rd ed.)

---
