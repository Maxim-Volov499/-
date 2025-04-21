# Определение структуры графа
G = {
    0: {'weight': 2},   # Вершина 0 с весом 2 кг
    1: {'weight': 3},   # Вершина 1 с весом 3 кг
    3: {'weight': 10},  # Вершина 3 с весом 10 кг
    2: {'weight': None}, 
    8: {'weight': None},
    4: {'weight': None},
    5: {'weight': None},
    6: {'weight': None},
    7: {'weight': None},  
    9: {'weight': None}   
}

def find_vertex_with_extra_weight(G, extra_weight):
    """Функция находит вершину с заданным лишним весом."""
    for vertex, data in G.items():
        if 'weight' in data and data['weight'] == extra_weight:
            return vertex
    return None

def sort_vertices_by_weight(G):
    """Функция сортирует вершины по весу."""
    # Преобразование None в максимальное возможное значение для правильной сортировки
    weights = []
    for vertex, data in G.items():
        weight = data.get('weight')
        if weight is None:
            weight = float('inf')  # Для вершин с неизвестным весом используем бесконечность
        weights.append((vertex, weight))
    
    return sorted(weights, key=lambda x: x[1])  # Сортируем по второму элементу кортежа (весу)

# Поиск вершины с лишним весом в 10 кг
extra_weight = 10
result_vertex = find_vertex_with_extra_weight(G, extra_weight)
if result_vertex is not None:
    print(f"Вершина с лишним весом {extra_weight} кг: {result_vertex}")
else:
    print(f"Вершина с лишним весом {extra_weight} кг не найдена.")

# Сортировка вершин по весу
sorted_vertices = sort_vertices_by_weight(G)
print("\nОтсортированные вершины по весу:")
for vertex, weight in sorted_vertices:
    if weight != float('inf'):  # Если вес не равен бесконечности, значит он известен
        print(f"{vertex}: {weight} кг")
    else:
        print(f"{vertex}: вес неизвестен")