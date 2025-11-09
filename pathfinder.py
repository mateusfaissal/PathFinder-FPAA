import heapq
from typing import List, Tuple, Optional, Set


class Node:
    
    def __init__(self, position: Tuple[int, int], parent: Optional['Node'] = None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __hash__(self):
        return hash(self.position)
    
    def __repr__(self):
        return f"Node({self.position}, f={self.f})"


class PathFinder:
    
    def __init__(self, maze: List[List]):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0]) if maze else 0
        self.start = None
        self.end = None
        
        self._find_start_end()
    
    def _find_start_end(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = str(self.maze[i][j]).upper()
                if cell == 'S':
                    self.start = (i, j)
                elif cell == 'E':
                    self.end = (i, j)
        
        if self.start is None:
            raise ValueError("Ponto inicial 'S' não encontrado no labirinto!")
        if self.end is None:
            raise ValueError("Ponto final 'E' não encontrado no labirinto!")
    
    def heuristic(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = position
        neighbors = []
        
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in movements:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                cell = str(self.maze[new_row][new_col]).upper()
                if cell in ['0', 'S', 'E']:
                    neighbors.append((new_row, new_col))
        
        return neighbors
    
    def find_path(self) -> Optional[List[Tuple[int, int]]]:
        start_node = Node(self.start)
        start_node.g = 0
        start_node.h = self.heuristic(self.start, self.end)
        start_node.f = start_node.g + start_node.h
        
        open_list = []
        heapq.heappush(open_list, start_node)
        closed_set: Set[Tuple[int, int]] = set()
        
        g_costs = {self.start: 0}
        
        while open_list:
            current_node = heapq.heappop(open_list)
            
            if current_node.position in closed_set:
                continue
            
            closed_set.add(current_node.position)
            
            if current_node.position == self.end:
                return self._reconstruct_path(current_node)
            
            for neighbor_pos in self.get_neighbors(current_node.position):
                if neighbor_pos in closed_set:
                    continue
                
                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = self.heuristic(neighbor_pos, self.end)
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                
                if neighbor_pos not in g_costs or neighbor_node.g < g_costs[neighbor_pos]:
                    g_costs[neighbor_pos] = neighbor_node.g
                    heapq.heappush(open_list, neighbor_node)
        
        return None
    
    def _reconstruct_path(self, node: Node) -> List[Tuple[int, int]]:
        path = []
        current = node
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path[::-1]
    
    def display_path(self, path: Optional[List[Tuple[int, int]]] = None):
        if path is None:
            print("\nLabirinto original:")
            for row in self.maze:
                print(' '.join(str(cell) for cell in row))
            return
        
        display_maze = [row[:] for row in self.maze]
        
        for i, (row, col) in enumerate(path):
            if i != 0 and i != len(path) - 1:
                display_maze[row][col] = '*'
        
        print("\nLabirinto com caminho destacado:")
        for row in display_maze:
            print(' '.join(str(cell) for cell in row))
    
    def format_path_output(self, path: List[Tuple[int, int]]) -> str:
        formatted = []
        for i, (row, col) in enumerate(path):
            if i == 0:
                formatted.append(f"s({row}, {col})")
            elif i == len(path) - 1:
                formatted.append(f"e({row}, {col})")
            else:
                formatted.append(f"({row}, {col})")
        
        return "[" + ", ".join(formatted) + "]"


def main():
    
    print("=" * 60)
    print("PathFinder - Algoritmo A* para Labirinto 2D")
    print("=" * 60)
    
    maze = [
        ['S', 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 'E', 1]
    ]
    
    print("\nExemplo 1: Labirinto do PDF")
    print("-" * 60)
    
    pathfinder = PathFinder(maze)
    
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    
    if path:
        print(f"\nMenor caminho encontrado com {len(path)} passos!")
        print(f"Coordenadas: {pathfinder.format_path_output(path)}")
        pathfinder.display_path(path)
    else:
        print("\nSem solução - não há caminho possível entre S e E.")
    
    print("\n" + "=" * 60)
    print("Exemplo 2: Labirinto sem solução")
    print("-" * 60)
    
    maze_no_solution = [
        ['S', 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 'E', 1]
    ]
    
    pathfinder2 = PathFinder(maze_no_solution)
    pathfinder2.display_path()
    
    path2 = pathfinder2.find_path()
    
    if path2:
        print(f"\nMenor caminho encontrado com {len(path2)} passos!")
        print(f"Coordenadas: {pathfinder2.format_path_output(path2)}")
        pathfinder2.display_path(path2)
    else:
        print("\nSem solução - não há caminho possível entre S e E.")
    
    print("\n" + "=" * 60)
    print("Exemplo 3: Labirinto maior")
    print("-" * 60)
    
    maze_large = [
        ['S', 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 'E']
    ]
    
    pathfinder3 = PathFinder(maze_large)
    pathfinder3.display_path()
    
    path3 = pathfinder3.find_path()
    
    if path3:
        print(f"\nMenor caminho encontrado com {len(path3)} passos!")
        print(f"Coordenadas: {pathfinder3.format_path_output(path3)}")
        pathfinder3.display_path(path3)
    else:
        print("\nSem solução - não há caminho possível entre S e E.")


if __name__ == "__main__":
    main()
