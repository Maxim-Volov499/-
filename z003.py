import numpy as np

def level_edges(edges, edge_weights, levels):
  """
  Разделяет список ребер на уровни на основе заданных весов ребер.

  Args:
    edges: Список кортежей, представляющих ребра графа (например, [(1, 2), (2, 3), ...]).
    edge_weights: Список весов, соответствующих ребрам (длина должна совпадать с длиной edges).
    levels: Количество уровней, на которые нужно разделить ребра.

  Returns:
    Список уровней, соответствующих ребрам.
  """

  if len(edges) != len(edge_weights):
    raise ValueError("Длина списка ребер и списка весов должна совпадать.")

  edge_weights = np.array(edge_weights) # Преобразуем в numpy array для удобства
  thresholds = np.linspace(edge_weights.min(), edge_weights.max(), levels + 1) # Создаем пороговые значения
  edge_levels = np.zeros(len(edges), dtype=int)  # Массив для хранения уровней ребер

  for i in range(levels):
    edge_levels[(edge_weights >= thresholds[i]) & (edge_weights < thresholds[i+1])] = i + 1 # Присваиваем уровни

  return edge_levels.tolist() # Возвращаем обычный список Python

# Пример использования
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)]
edge_weights = [1.5, 3.2, 6.8, 2.1, 5.9]
levels = 3

edge_levels = level_edges(edges, edge_weights, levels)
print(f"Ребра: {edges}")
print(f"Веса ребер: {edge_weights}")
print(f"Уровни ребер: {edge_levels}")