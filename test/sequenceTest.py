import unittest
import sys
sys.path.append("../")
from core.sequence import Sequence, SequenceOrganizer

class SequenceTest(unittest.TestCase):

    def test01(self):
        a = Sequence("a", before = "c")
        b = Sequence("b", after = "d")
        c = Sequence("c", )
        d = Sequence("d", before = "a", after = "c")
        unsorted = [a, b, c, d]

        # d and a are in conflict
        self.assertRaises(SystemExit, SequenceOrganizer, unsorted)


    def test02(self):
        a = Sequence("a", before = "c")
        b = Sequence("b", after = "d")
        c = Sequence("c", before = "b")
        d = Sequence("d", before = "a")

        unsorted = [a, b, c, d]
        expected = [d, a, c, b]

        organizer = SequenceOrganizer(unsorted)
        sorted = organizer.getSortedList()

        self.assertTrue(sorted == expected)


    def test03(self):
        a = Sequence("a")
        b = Sequence("b", before = "a")
        c = Sequence("c", before = "b")
        d = Sequence("d", before = "c")

        unsorted = [a, b, c, d]
        expected = [d, c, b, a]

        organizer = SequenceOrganizer(unsorted)
        sorted = organizer.getSortedList()

        self.assertTrue(sorted == expected)


    def test04(self):
        d = Sequence("d", after = "c")
        c = Sequence("c", after = "b")
        b = Sequence("b", after = "a")
        a = Sequence("a")

        unsorted = [d, c, b, a]
        expected = [a, b, c, d]

        organizer = SequenceOrganizer(unsorted)
        sorted = organizer.getSortedList()

        self.assertTrue(sorted == expected)


    def test05(self):
        g = Sequence("g", after = "e")
        f = Sequence("f", before = "g", after = "e")
        e = Sequence("e", after = "c")
        d = Sequence("d", before = "e", after = "c")
        c = Sequence("c", after = "a")
        b = Sequence("b", before = "c", after = "a")
        a = Sequence("a")

        unsorted = [g, f, e, d, c, b, a]
        expected = [a, b, c, d, e, f, g]

        organizer = SequenceOrganizer(unsorted)
        sorted = organizer.getSortedList()

        self.assertTrue(sorted == expected)


if __name__ == '__main__':
    unittest.main()

