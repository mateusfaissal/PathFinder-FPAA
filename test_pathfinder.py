"""
Testes adicionais para o PathFinder
"""

from pathfinder import PathFinder


def test_labirinto_simples():
    """Teste com labirinto simples 3x3"""
    print("Teste 1: Labirinto simples 3x3")
    print("-" * 60)
    
    maze = [
        ['S', 0, 0],
        [0, 1, 0],
        [0, 0, 'E']
    ]
    
    pathfinder = PathFinder(maze)
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    if path:
        print(f"\n✓ Caminho encontrado: {pathfinder.format_path_output(path)}")
        print(f"  Número de passos: {len(path)}")
        pathfinder.display_path(path)
    else:
        print("\n✗ Sem solução")
    print()


def test_labirinto_direto():
    """Teste com caminho direto"""
    print("Teste 2: Caminho direto (linha reta)")
    print("-" * 60)
    
    maze = [
        ['S', 0, 0, 0, 'E']
    ]
    
    pathfinder = PathFinder(maze)
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    if path:
        print(f"\n✓ Caminho encontrado: {pathfinder.format_path_output(path)}")
        print(f"  Número de passos: {len(path)}")
        pathfinder.display_path(path)
    else:
        print("\n✗ Sem solução")
    print()


def test_labirinto_complexo():
    """Teste com labirinto mais complexo"""
    print("Teste 3: Labirinto complexo com múltiplos caminhos")
    print("-" * 60)
    
    maze = [
        ['S', 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 'E']
    ]
    
    pathfinder = PathFinder(maze)
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    if path:
        print(f"\n✓ Caminho encontrado: {pathfinder.format_path_output(path)}")
        print(f"  Número de passos: {len(path)}")
        pathfinder.display_path(path)
    else:
        print("\n✗ Sem solução")
    print()


def test_labirinto_espiral():
    """Teste com labirinto em espiral"""
    print("Teste 4: Labirinto em espiral")
    print("-" * 60)
    
    maze = [
        ['S', 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 'E']
    ]
    
    pathfinder = PathFinder(maze)
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    if path:
        print(f"\n✓ Caminho encontrado: {pathfinder.format_path_output(path)}")
        print(f"  Número de passos: {len(path)}")
        pathfinder.display_path(path)
    else:
        print("\n✗ Sem solução")
    print()


def test_inicio_fim_adjacentes():
    """Teste onde início e fim são adjacentes"""
    print("Teste 5: Início e fim adjacentes")
    print("-" * 60)
    
    maze = [
        ['S', 'E'],
        [0, 0]
    ]
    
    pathfinder = PathFinder(maze)
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    if path:
        print(f"\n✓ Caminho encontrado: {pathfinder.format_path_output(path)}")
        print(f"  Número de passos: {len(path)}")
        pathfinder.display_path(path)
    else:
        print("\n✗ Sem solução")
    print()


def test_labirinto_grande():
    """Teste com labirinto grande"""
    print("Teste 6: Labirinto grande (10x10)")
    print("-" * 60)
    
    maze = [
        ['S', 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 'E']
    ]
    
    pathfinder = PathFinder(maze)
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    if path:
        print(f"\n✓ Caminho encontrado: {pathfinder.format_path_output(path)}")
        print(f"  Número de passos: {len(path)}")
        pathfinder.display_path(path)
    else:
        print("\n✗ Sem solução")
    print()


def test_labirinto_bloqueado_parcial():
    """Teste com caminho muito estreito"""
    print("Teste 7: Caminho estreito (gargalo)")
    print("-" * 60)
    
    maze = [
        ['S', 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 'E']
    ]
    
    pathfinder = PathFinder(maze)
    pathfinder.display_path()
    
    path = pathfinder.find_path()
    if path:
        print(f"\n✓ Caminho encontrado: {pathfinder.format_path_output(path)}")
        print(f"  Número de passos: {len(path)}")
        pathfinder.display_path(path)
    else:
        print("\n✗ Sem solução")
    print()


def main():
    """Executa todos os testes"""
    print("=" * 60)
    print("TESTES DO PATHFINDER - ALGORITMO A*")
    print("=" * 60)
    print()
    
    test_labirinto_simples()
    test_labirinto_direto()
    test_labirinto_complexo()
    test_labirinto_espiral()
    test_inicio_fim_adjacentes()
    test_labirinto_grande()
    test_labirinto_bloqueado_parcial()
    
    print("=" * 60)
    print("TODOS OS TESTES CONCLUÍDOS")
    print("=" * 60)


if __name__ == "__main__":
    main()
