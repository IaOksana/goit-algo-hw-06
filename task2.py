'''Task 2
Write a program that uses the DFS and BFS algorithms to find paths in the graph that you developed 
in the first task.
Then compare the results of both algorithms for this graph, highlighting the difference in the 
paths obtained. Please explain why the paths for the algorithms are the way they are.
- Implement the DFS and BFS algorithms for finding paths in the graph developed in the first task.
- The results of the algorithms for this graph are compared, and the difference in the obtained paths 
is explained. The reasons why the algorithms have chosen such paths are explained.
- The conclusions are written in the form of a readme.md file for homework.'''

import networkx as nx
from graph_utils import create_graph

def generate_readme_dfs_bfs(dfs_path_result, bfs_path_result):
    """Генерує readme.md файл з результатами порівняння DFS та BFS."""

    readme_content = f"""
# Порівняння алгоритмів DFS та BFS для пошуку шляху в графі

## Результати

**Шлях, знайдений DFS:** {dfs_path_result}
**Шлях, знайдений BFS:** {bfs_path_result}

## Аналіз

DFS (Depth-First Search) та BFS (Breadth-First Search) - це два фундаментальні алгоритми пошуку в графах. 
Вони відрізняються способом обходу графа та, як наслідок, шляхами, які вони знаходять.

**DFS**  працює рекурсивно, досліджуючи граф "в глибину". Він починає з початкової вершини і рухається вздовж 
одного з її ребер до наступної вершини. Потім він продовжує рухатися вздовж ребер, поки не досягне вершини, 
з якої немає невідвіданих ребер. У цьому випадку DFS повертається назад і досліджує інші ребра початкової вершини.

**BFS**  працює ітеративно, досліджуючи граф "в ширину". Він починає з початкової вершини і відвідує всі її сусідів. 
Потім він відвідує всіх сусідів сусідів і так далі, поки не знайде цільову вершину.

**Різниця в отриманих шляхах:**

У даному випадку, **DFS** знайшов шлях: {dfs_path_result}.  Цей шлях не є найкоротшим, 
оскільки DFS досліджує граф в глибину, не враховуючи відстань до цільової вершини.

**BFS** знайшов шлях: {bfs_path_result}. Цей шлях є найкоротшим, оскільки BFS досліджує граф в ширину, 
гарантуючи, що він знайде цільову вершину з найменшою кількістю кроків.

## Висновки

- **DFS** може знайти будь-який шлях між двома вершинами, але не гарантує знаходження найкоротшого.
- **BFS** гарантує знаходження найкоротшого шляху між двома вершинами, але може зайняти більше часу, 
ніж DFS, особливо у великих графах.
- Вибір алгоритму залежить від конкретної задачі та вимог до швидкості та оптимальності пошуку.


    """

    with open('readme.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("Файл readme.md створено.")

def dfs_path(graph, start_node, end_node):
    """Finds a path between two nodes using Depth-First Search (DFS)."""
    visited = set()
    stack = [(start_node, [start_node])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == end_node:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))
    return None

def bfs_path(graph, start_node, end_node):
    """Finds a path between two nodes using Breadth-First Search (BFS)."""
    visited = set()
    queue = [(start_node, [start_node])]
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            if vertex == end_node:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                 queue.append((neighbor, path + [neighbor]))
    return None

def main():
    # Create the graph
    graph = create_graph()

    # Find paths between Alice and Frank using DFS and BFS
    dfs_path_result = dfs_path(graph, 'A', 'I')
    bfs_path_result = bfs_path(graph, 'A', 'I')

    print("DFS path:", dfs_path_result)
    print("BFS path:", bfs_path_result)

    generate_readme_dfs_bfs(dfs_path_result, bfs_path_result)


if __name__ == "__main__":
    main()