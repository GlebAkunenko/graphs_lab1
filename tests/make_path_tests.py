from unittest import TestCase

from challange.utils import make_path

class MakePathTests(TestCase):

    def test_abcd(self):
        edges = [
            ('a', 'b', 1),
            ('b', 'c', 1),
            ('c', 'd', 1),
            ('d', 'e', 1),
            ('e', 'f', 1),
            ('f', 'g', 1),
            ('g', 'k', 1),
        ]
        self.assertEquals(
            "c",
            make_path(edges, 'c',1)
        )
        self.assertEquals(
            "c d",
            make_path(edges, 'c',2)
        )
        self.assertEquals(
            "c d e f g",
            make_path(edges, 'c',5)
        )

