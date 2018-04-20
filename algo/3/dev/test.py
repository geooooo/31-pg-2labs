from copy import deepcopy as copy
import ctypes
ograph = ctypes.CDLL("./ograph.so")

# Адаптация структур

class ograph_Vertex(ctypes.Structure):
    pass

class ograph_VertexList(ctypes.Structure):
    pass

ograph_Vertex._fields_ = [
    ("value", ctypes.py_object),
    ("next", ctypes.POINTER(ograph_Vertex)),
    ("vertex_list", ctypes.POINTER(ograph_VertexList)),
]

ograph_VertexList._fields_ = [
    ("vertex", ctypes.POINTER(ograph_Vertex)),
    ("next", ctypes.POINTER(ograph_VertexList)),
]

# Адаптация возвращаемых значений функций

ograph.ograph_create_vertex.restype = ctypes.POINTER(ograph_Vertex)
ograph.ograph_create_vertex_list.restype = ctypes.POINTER(ograph_VertexList)

# Класс графа

class OGraph:
    """
        Ориентированный граф
    """

    # Вершина графа
    _NODE = {
        "ograph_vertex": None,
        "id": None,
    }


    def __init

# Обёртки над функциями

# def create_graph():
#     vertex = create_vertex(value)
#     vertex.contents.vertex_list = create_vertex_list(vertexs)
#     return vertex

def create_vertex(value):
    vertex = ograph.ograph_create_vertex()
    vertex.contents.value = value
    return vertex

def create_vertex_list(vertexs=[]):
    if vertexs:
        l = len(vertexs)
        vertexs = (ctypes.POINTER(ograph_Vertex) * l)(*vertexs)
        print(vertexs)
        vertex_list = ograph.ograph_create_vertex_list(vertexs, ctypes.c_int(l))
    else:
        vertex_list = ograph.ograph_create_vertex_list(ctypes.c_void_p(), 0)
    # print(vertexs, l)
    return vertex_list

def free_vertex(graph):
    ograph.ograph_free_vertex(graph)

def add(graph, vertex):
    ograph.ograph_add(graph, vertex)

def rem(graph, vertex):
    ograph.ograph_del(graph, vertex)

def is_exists_edge(graph, vertex1, vertex2):
    return bool(ctypes.c_bool(ograph.ograph_is_exists_edge(graph, vertex1, vertex2)))

# Тестовый код

graph = a = create_vertex("A")
b = create_vertex("B")
c = create_vertex("C")
d = create_vertex("D")
e = create_vertex("E")
f = create_vertex("F")

a.contents.vertex_list = create_vertex_list([b, c, d])
b.contents.vertex_list = create_vertex_list([e, f])
c.contents.vertex_list = create_vertex_list([d])
d.contents.vertex_list = create_vertex_list([a])
e.contents.vertex_list = create_vertex_list([c])
f.contents.vertex_list = create_vertex_list()

# add(graph, b)
# add(graph, c)
# add(graph, d)
# add(graph, e)
# add(graph, f)

# print(a.contents.value)
# print(b.contents.value)
# print(c.contents.value)
# print(d.contents.value)
# print(e.contents.value)
# print(f.contents.value)

# print(a.contents.vertex_list)
# print(b.contents.vertex_list)
# print(c.contents.vertex_list)
# print(d.contents.vertex_list)
# print(e.contents.vertex_list)
# print(f.contents.vertex_list)

# print(a.contents.vertex_list.contents.vertex.contents)
# print(b.contents.vertex_list.contents.vertex.contents.value)
# print(c.contents.vertex_list.contents.vertex.contents.value)
# print(d.contents.vertex_list.contents.vertex.contents.value)
# print(e.contents.vertex_list.contents.vertex.contents.value)
# print(f.contents.vertex_list.contents.vertex.contents.value)

free_vertex(a)
free_vertex(b)
free_vertex(c)
free_vertex(d)
free_vertex(e)
free_vertex(f)
