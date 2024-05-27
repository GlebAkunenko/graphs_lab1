from unittest import TestCase
from lattices.hexagonal import make_grip, titles, make_graph

class GripTests(TestCase):

    def test_6x6(self):
        expected = [
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0]
        ]
        actual = make_grip(6, 6)
        self.assertListEqual(expected, actual)


class TitleTests(TestCase):

    def test_0(self):
        G = titles(3, 6)
        actual = G(0, 0)
        expected = "0"
        self.assertEquals(expected, actual)


    def test_1(self):
        G = titles(3, 6)
        actual = G(0, 1)
        expected = "1"
        self.assertEquals(expected, actual)


    def test_2(self):
        G = titles(3, 6)
        actual = G(0, 2)
        expected = "2"
        self.assertEquals(expected, actual)


    def test_5(self):
        G = titles(3, 6)
        actual = G(0, 5)
        expected = "5"
        self.assertEquals(expected, actual)


    def test_6(self):
        G = titles(3, 6)
        actual = G(1, 0)
        expected = "6"
        self.assertEquals(expected, actual)


    def test_11(self):
        G = titles(3, 6)
        actual = G(1, 5)
        expected = "11"
        self.assertEquals(expected, actual)


    def test_7(self):
        G = titles(3, 6)
        actual = G(1, 1)
        expected = "7"
        self.assertEquals(expected, actual)


class GraphTest(TestCase):

    def test_6x6(self):
        edges = [
            ("1", "6", 1),
            ("1", "8", 1),
            ("3", "8", 1),
            ("3", "10", 1),
            ("5", "10", 1),
            ("6", "12", 1),
            ("8", "14", 1),
            ("10", "16", 1),
            ("12", "19", 1),
            ("14", "19", 1),
            ("14", "21", 1),
            ("16", "21", 1),
            ("16", "23", 1)
        ]
        expected = edges + [(v, u, 1) for (u, v, w) in edges]
        actual = make_graph(4, 6, True)
        self.assertSetEqual(set(expected), set(actual))

    def test_6x6_di(self):
        edges = [
            ("1", "6", 1),
            ("1", "8", 1),
            ("3", "8", 1),
            ("3", "10", 1),
            ("5", "10", 1),
            ("6", "12", 1),
            ("8", "14", 1),
            ("10", "16", 1),
            ("12", "19", 1),
            ("14", "19", 1),
            ("14", "21", 1),
            ("16", "21", 1),
            ("16", "23", 1)
        ]
        actual = make_graph(4, 6)
        self.assertSetEqual(set(edges), set(actual))
