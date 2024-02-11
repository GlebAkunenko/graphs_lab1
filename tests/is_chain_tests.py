from unittest import TestCase

from problems import is_chain
import representations as graphs

class IsChainTests(TestCase):

    def setUp(self):
        self.matrix =  [[0, 1, 1, 0, 0, 0, 2, 0],
                        [1, 0, 1, 0, 2, 0, 1, 0],
                        [0, 0, 0, 0, 5, 0, 0, 0],
                        [4, 0, 0, 0, 0, 0, 3, 2],
                        [0, 0, 0, 0, 0, 12, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 5, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]]
        self.labels = [f"x{i}" for i in range(1, 8+1)]


    def test_matrix(self):
        self.assertTrue(is_chain.from_matrix(self.matrix, self.labels, "x4 x1 x2 x7 x5 x6"))
        self.assertFalse(is_chain.from_matrix(self.matrix, self.labels, "x4 x1 x2 x7 x5 x3"))
        self.assertFalse(is_chain.from_matrix(self.matrix, self.labels, "x1 x2 x1 x2"))
        self.assertTrue(is_chain.from_matrix(self.matrix, self.labels, "x1 x2 x1"))

    def test_edges(self):
        edges = graphs.edge_list_from_matrix(self.matrix, self.labels)
        self.assertTrue(is_chain.from_edge_list(edges, "x4 x1 x2 x7 x5 x6"))
        self.assertFalse(is_chain.from_edge_list(edges, "x4 x1 x2 x7 x5 x3"))
        self.assertFalse(is_chain.from_edge_list(edges, "x1 x2 x1 x2"))
        self.assertTrue(is_chain.from_edge_list(edges, "x1 x2 x1"))

    def test_nodes(self):
        nodes = graphs.node_records_from_matrix(self.matrix, self.labels)
        self.assertTrue(is_chain.from_node_records(nodes, "x4 x1 x2 x7 x5 x6"))
        self.assertFalse(is_chain.from_node_records(nodes, "x4 x1 x2 x7 x5 x3"))
        self.assertFalse(is_chain.from_node_records(nodes, "x1 x2 x1 x2"))
        self.assertTrue(is_chain.from_node_records(nodes, "x1 x2 x1"))


