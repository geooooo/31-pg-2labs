#include "ograph.h"



/*
    Вывод сообщения об ошибке и аварийное
    завершение программы
*/
void ograph_error(char* message)
{
    printf("Error: %s !", message);
    exit(EXIT_FAILURE);
}



/*
    Создание вершины графа
    return - граф из одной "пустой" вершины
*/
ograph_Vertex* ograph_create_vertex(void)
{
    ograph_Vertex* vertex = (ograph_Vertex*)malloc(sizeof(ograph_Vertex));
    if (vertex == NULL) {
        ograph_error(ograph_E_MEMORY_ALLOC);
    }
    vertex->value = ograph_NONE_VALUE;
    vertex->next  = NULL;
    return vertex;
}



/*
    Создание списка указателей на вершины графа
    vertexs - список указателей на смежные вершины
    count   - количество вершин
    return  - список смежных вершин какой-то вершины
*/
ograph_VertexList* ograph_create_vertex_list(ograph_Vertex* vertexs[], int count)
{
    if (count == 0) {
        return NULL;
    }
    ograph_VertexList* vertex_list = (ograph_VertexList*)malloc(sizeof(ograph_VertexList));
    if (vertex_list == NULL) {
        ograph_error(ograph_E_MEMORY_ALLOC);
    }
    vertex_list->vertex = vertexs[0];
    ograph_VertexList* _vertex_list = vertex_list;
    for (int i = 1; i < count; i++) {
        _vertex_list->next = (ograph_VertexList*)malloc(sizeof(ograph_VertexList));
        if (_vertex_list->next == NULL) {
            ograph_error(ograph_E_MEMORY_ALLOC);
        }
        _vertex_list->next->vertex = vertexs[i];
        _vertex_list = _vertex_list->next;
    }
    _vertex_list->next  = NULL;
    return vertex_list;
}



/*
    Очистка памяти, занятую под вершину
    graph - первая вершина графа
*/
void ograph_free_vertex(ograph_Vertex* graph)
{
    if (graph == NULL) {
        return;
    }
    ograph_Vertex* cur = graph;
    ograph_Vertex* next = cur->next;
    while (true) {
        ograph_free_vertex_list(cur->vertex_list);
        free(cur);
        cur = next;
        if (next == NULL) {
            break;
        }
        next = next->next;
    }
}



/*
    Очистка памяти, занятую под список указателей на вершины
    vertex_list - список указателей на вершины
*/
void ograph_free_vertex_list(ograph_VertexList* vertex_list)
{
    if (vertex_list == NULL) {
        return;
    }
    ograph_VertexList* cur = vertex_list;
    ograph_VertexList* next = cur->next;
    while (true) {
        free(cur);
        cur = next;
        if (next == NULL) {
            break;
        }
        next = next->next;
    }
}



/*
    Добавление вершины в граф
    graph  - первая вершина графа
    vertex - указатель на добавляемую вершину
*/
void ograph_add(ograph_Vertex** graph, ograph_Vertex* vertex)
{
    vertex->next = *graph;
    *graph = vertex;
}



/*
    Удаление вершины из графа
    graph  - первая вершина графа
    vertex - указатель на удаляемую вершину
*/
void ograph_del(ograph_Vertex** graph, ograph_Vertex* vertex)
{
    ograph_Vertex* cur = *graph;
    ograph_Vertex* prev = NULL;
    while (cur != NULL) {
        if (cur == vertex) {
            if (prev == NULL) {
                // Если искомая вершина - первая в графе
                *graph = cur->next;
            } else {
                prev->next = cur->next;
            }
            ograph_del_from_vertex_list(graph, vertex);
            return;
        }
        prev = cur;
        cur = cur->next;
    }
}



void ograph_del_from_vertex_list(ograph_Vertex** graph, ograph_Vertex* vertex)
{
    ograph_Vertex* _graph = *graph;
    while (_graph != NULL) {
        ograph_VertexList* _vertex_list = _graph->vertex_list;
        ograph_VertexList* prev_vertex_list = NULL;

        // Поиск удаляемой вершины
        while (_vertex_list != NULL) {
            if (_vertex_list->vertex == vertex) {
                if (prev_vertex_list == NULL) {
                    // Если искомая вершина - первая
                    _graph->vertex_list = _graph->vertex_list->next;
                } else {
                    prev_vertex_list->next = _vertex_list->next;
                }
                return;
            }
            prev_vertex_list = _vertex_list;
            _vertex_list = _vertex_list->next;
        }

        _graph = _graph->next;
    }
}



/*
    Проверка смежности указаных вершин графа
    graph            - первая вершина графа
    vertex1, vertex2 - вершины, для которых осуществляется проверка
    return           - смежные ли вершины
*/
bool ograph_is_exists_edge(ograph_Vertex* graph, ograph_Vertex* vertex1, ograph_Vertex* vertex2)
{
    // Проверка принадлежности вершин графу
    if (!ograph_is_vertex_in_graph(graph, vertex1) ||
        !ograph_is_vertex_in_graph(graph, vertex2))
    {
        return false;
    }
    // Проверка смежности вершин
    ograph_VertexList* cur = vertex1->vertex_list;
    while (cur != NULL) {
        if (cur->vertex == vertex2) {
            return true;
        }
        cur = cur->next;
    }
    cur = vertex2->vertex_list;
    while (cur != NULL) {
        if (cur->vertex == vertex1) {
            return true;
        }
        cur = cur->next;
    }
    return false;
}


/*
    Проверка принадлежности вершины графу
    graph  - первая вершина графа
    vertex - вершина, для которой ведётся проверка
    return - принадлежит ли вершина графу
*/
bool ograph_is_vertex_in_graph(ograph_Vertex* graph, ograph_Vertex* vertex)
{
    ograph_Vertex* cur = graph;
    while (cur != NULL) {
        if (cur == vertex) {
            return true;
        }
        cur = cur->next;
    }
    return false;
}
