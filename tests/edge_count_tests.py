from unittest import TestCase

import representations as graphs
from problems import edge_count

class EdgeCountTests(TestCase):

    def setUp(self):
        self.data_12 = [
            [0, 1, 1, 0, 0, 0, 2, 0],
            [0, 0, 1, 0, 2, 0, 1, 0],
            [0, 0, 0, 0, 5, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 3, 2],
            [0, 0, 0, 0, 0, 12, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
        self.data_10 = [
            [ 0, 0, 1, 0, 0, 0, 2, 0],
            [ 0, 0, 1, 0, 2, 0, 1, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 4, 0, 0, 0, 0, 0, 3, 2],
            [ 0, 0, 0, 0, 0, 12, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 5, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0]]
        self.data_0 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.data_9 = [
            [1, 1, 1],
            [10, 1, 1],
            [1, 1, 2],
        ]
        self.labels_12 = [str(i) for i in range(8**2)]
        self.labels_10 = [str(i) for i in range(8**2)]
        self.labels_9 = [str(i) for i in range(3**2)]
        self.labels_0 = [str(i) for i in range(3**2)]


    def test_matrix(self):
        self.assertEquals(edge_count.from_matrix(self.data_12), 12)
        self.assertEquals(edge_count.from_matrix(self.data_10), 10)
        self.assertEquals(edge_count.from_matrix(self.data_9), 9)
        self.assertEquals(edge_count.from_matrix(self.data_0), 0)

    def test_edge_list(self):
        self.assertEquals(edge_count.from_edge_list(graphs.edge_list_from_matrix(self.data_12, self.labels_12)), 12)
        self.assertEquals(edge_count.from_edge_list(graphs.edge_list_from_matrix(self.data_10, self.labels_10)), 10)
        self.assertEquals(edge_count.from_edge_list(graphs.edge_list_from_matrix(self.data_9, self.labels_9)), 9)
        self.assertEquals(edge_count.from_edge_list(graphs.edge_list_from_matrix(self.data_0, self.labels_0)), 0)

    def test_node_records(self):
        self.assertEquals(edge_count.from_node_records(graphs.node_records_from_matrix(self.data_12, self.labels_12)), 12)
        self.assertEquals(edge_count.from_node_records(graphs.node_records_from_matrix(self.data_10, self.labels_10)), 10)
        self.assertEquals(edge_count.from_node_records(graphs.node_records_from_matrix(self.data_9, self.labels_9)), 9)
        self.assertEquals(edge_count.from_node_records(graphs.node_records_from_matrix(self.data_0, self.labels_0)), 0)