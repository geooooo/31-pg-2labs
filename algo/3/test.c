#include <stdio.h>
#include <stdlib.h>

#include "ograph.h"



void test_case1(void);



int main(void) {

    test_case1();
    return EXIT_SUCCESS;

}



void test_case1(void)
{
    ograph_Vertex* a = ograph_create_vertex();
    a->value = 'A';

    ograph_Vertex* graph = a;

    ograph_Vertex* b = ograph_create_vertex();
    b->value = 'B';

    ograph_Vertex* c = ograph_create_vertex();
    c->value = 'C';

    ograph_Vertex* d = ograph_create_vertex();
    d->value = 'D';

    ograph_Vertex* e = ograph_create_vertex();
    e->value = 'E';

    ograph_Vertex* f = ograph_create_vertex();
    f->value = 'F';

    ograph_Vertex* x = ograph_create_vertex();
    x->value = 'X';

    ograph_Vertex* vla[] = {b, c, d};
    a->vertex_list = ograph_create_vertex_list(vla, 3);

    ograph_Vertex* vlb[] = {e, f};
    b->vertex_list = ograph_create_vertex_list(vlb, 2);

    ograph_Vertex* vlc[] = {d};
    c->vertex_list = ograph_create_vertex_list(vlc, 1);

    ograph_Vertex* vld[] = {a};
    d->vertex_list = ograph_create_vertex_list(vld, 1);

    ograph_Vertex* vle[] = {c};
    e->vertex_list = ograph_create_vertex_list(vle, 1);

    f->vertex_list = ograph_create_vertex_list(NULL, 0);

    ograph_add(&graph, b);
    ograph_add(&graph, c);
    ograph_add(&graph, d);
    ograph_add(&graph, e);
    ograph_add(&graph, f);

    ograph_del(&graph, b);
    ograph_del(&graph, a);
    // ograph_del(&graph, d);

    ograph_Vertex* _graph = graph;
    while (_graph != NULL) {
        printf("Vertex: %c\n", _graph->value);
        printf("VertexList: ");
        ograph_VertexList* vertex_list = _graph->vertex_list;
        while (vertex_list != NULL) {
            printf("%c ", vertex_list->vertex->value);
            vertex_list = vertex_list->next;
        }
        _graph = _graph->next;
        printf("\n\n");
    }

    ograph_free_vertex(graph);
    ograph_free_vertex(x);
}
