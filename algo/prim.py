def prim(graph: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    all_nodes = {u for (u, v, w) in graph}.union(v for (u, v, w) in graph)
    nodes = {graph[0][0]}
    current_edges = set(graph)
    answer = []
    while len(nodes) < len(all_nodes):
        min_edge = max({
            (u, v, w)
            for (u, v, w) in current_edges
            if (u in nodes and v not in nodes)
            or (v in nodes and u not in nodes)
        },
            key=lambda x: x[2])
        current_edges.remove(min_edge)
        if min_edge[0] not in nodes:
            nodes.add(min_edge[0])
        else:
            nodes.add(min_edge[1])
        answer.append(min_edge)
        print(len(nodes), len(all_nodes))
        print(all_nodes.difference(nodes))
        a = all_nodes.difference(nodes)
        b = nodes.difference(all_nodes)
        if len(nodes) == 65:
            pass

    return answer

