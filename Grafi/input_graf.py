import networkx
import matplotlib.pyplot as plt


def input_edges_list():
    """????????? ?????? ????? ? ?????:
    ? ?????? ?????? N - ????? ?????,
    ????? ??????? N ????? ?? ???? ???? ? ?????? ?????
    ????? - ???????? ??????, ????? ?????, ? ????? - ??? ???

    return ???? ? ????? ??????? ???????? ????????? ? ??????"""
    N = int(input('??????? ?????????? ?????:'))
    G = {}
    for i in range(N):
        vertex1, vertex2, weight = input().split()
        weight = float(weight)
        # ???????? ????? (vertex1, vertex2)
        if vertex1 not in G:
            G[vertex1] = {vertex2:weight}
        else:  # ?????? ????? ??????? ??? ???????????
            G[vertex1][vertex2] = weight
        # ???? ?? ????????????, ??????? ???????? ????? (vertex2, vertex1)
        if vertex2 not in G:
            G[vertex2] = {vertex1:weight}
        else:  # ?????? ????? ??????? ??? ???????????
            G[vertex2][vertex1] = weight
    return G


A = networkx.Graph(input_edges_list())
position = networkx.spring_layout(A) # positions for all nodes
networkx.draw(A, position)
networkx.draw_networkx_labels(A, position)
#networkx.draw_networkx_edge_labels(A, position, edge_labels=)


plt.show() # display