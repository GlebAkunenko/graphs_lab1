from unittest import TestCase

import representations
from problems import nodes_by_sum
from data import matrix, labels

class NodesBySumTests(TestCase):

    def setUp(self):
        self.matrix = matrix
        self.labels = labels

    def test_matrix(self):
        self.assertCountEqual(
            nodes_by_sum.from_matrix(matrix, labels, 10),
            ['x7', 'x5', 'x6']
        )
        self.assertCountEqual(
            nodes_by_sum.from_matrix(matrix, labels, 100),
            []
        )
        self.assertCountEqual(
            nodes_by_sum.from_matrix(matrix, labels, 1),
            ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
        )
        self.assertCountEqual(
            nodes_by_sum.from_matrix(matrix, labels, 7),
            ['x7', 'x5', 'x6', 'x1', 'x4']
        )


    def test_edge_list(self):
        edges = graphs.edge_list_from_matrix(matrix, labels)
        self.assertCountEqual(
            nodes_by_sum.from_edge_list(edges, labels, 10),
            ['x7', 'x5', 'x6']
        )
        self.assertCountEqual(
            nodes_by_sum.from_edge_list(edges, labels, 100),
            []
        )
        self.assertCountEqual(
            nodes_by_sum.from_edge_list(edges, labels, 1),
            ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
        )
        self.assertCountEqual(
            nodes_by_sum.from_edge_list(edges, labels, 7),
            ['x7', 'x5', 'x6', 'x1', 'x4']
        )

    def test_node_records(self):
        nodes = graphs.node_records_from_matrix(matrix, labels)
        self.assertCountEqual(
            nodes_by_sum.from_node_records(nodes, 10),
            ['x7', 'x5', 'x6']
        )
        self.assertCountEqual(
            nodes_by_sum.from_node_records(nodes,100),
            []
        )
        self.assertCountEqual(
            nodes_by_sum.from_node_records(nodes,1),
            ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
        )
        self.assertCountEqual(
            nodes_by_sum.from_node_records(nodes, 7),
            ['x7', 'x5', 'x6', 'x1', 'x4']
        )