#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdbool.h>



#define ograph_NONE_VALUE       '\0'

#define ograph_E_MEMORY_ALLOC   "memory allocation"



/* Значение, хранящееся в вершине графа */
typedef void* ograph_Value;

typedef struct _Vertex ograph_Vertex;
typedef struct _VertexList ograph_VertexList;

/* Список связей вершины графа с другими вершинами */
struct _VertexList {
    ograph_VertexList* next;
    ograph_Vertex* vertex;
};

/* Вершина графа */
struct _Vertex {
    ograph_Value value;
    ograph_Vertex* next;
    ograph_VertexList* vertex_list;
};




ograph_Vertex* ograph_create_vertex(void);

ograph_VertexList* ograph_create_vertex_list(ograph_Vertex* vertexs[], int count);

void ograph_free_vertex(ograph_Vertex* graph);

void ograph_add(ograph_Vertex** graph, ograph_Vertex*);

void ograph_del(ograph_Vertex** graph, ograph_Vertex*);

bool ograph_is_exists_edge(ograph_Vertex* graph, ograph_Vertex*, ograph_Vertex*);

static bool ograph_is_vertex_in_graph(ograph_Vertex* graph, ograph_Vertex*);

static void ograph_free_vertex_list(ograph_VertexList*);

static void ograph_error(char* message);
