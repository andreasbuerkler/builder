import unittest
import sys
import os
sys.path.append(os.getcwd()+"/../")
from builder.core.sequence import Sequence, SequenceOrganizer

class SequenceTest(unittest.TestCase):

    def test_01(self):
        a = Sequence("a", before = "c")
        b = Sequence("b", after = "d")
        c = Sequence("c", )
        d = Sequence("d", before = "a", after = "c")
        unsortedList = [a, b, c, d]

        # d and a are in conflict
        self.assertRaises(SystemExit, SequenceOrganizer, unsortedList)


    def test_02(self):
        a = Sequence("a", before = "c")
        b = Sequence("b", after = "d")
        c = Sequence("c", before = "b")
        d = Sequence("d", before = "a")

        unsortedList = [a, b, c, d]
        expected = [d, a, c, b]

        organizer = SequenceOrganizer(unsortedList)
        sortedList = organizer.getSortedList()

        self.assertTrue(sortedList == expected)


    def test_03(self):
        a = Sequence("a")
        b = Sequence("b", before = "a")
        c = Sequence("c", before = "b")
        d = Sequence("d", before = "c")

        unsortedList = [a, b, c, d]
        expected = [d, c, b, a]

        organizer = SequenceOrganizer(unsortedList)
        sortedList = organizer.getSortedList()

        self.assertTrue(sortedList == expected)


    def test_04(self):
        d = Sequence("d", after = "c")
        c = Sequence("c", after = "b")
        b = Sequence("b", after = "a")
        a = Sequence("a")

        unsortedList = [d, c, b, a]
        expected = [a, b, c, d]

        organizer = SequenceOrganizer(unsortedList)
        sortedList = organizer.getSortedList()

        self.assertTrue(sortedList == expected)


    def test_05(self):
        g = Sequence("g", after = "e")
        f = Sequence("f", before = "g", after = "e")
        e = Sequence("e", after = "c")
        d = Sequence("d", before = "e", after = "c")
        c = Sequence("c", after = "a")
        b = Sequence("b", before = "c", after = "a")
        a = Sequence("a")

        unsortedList = [g, f, e, d, c, b, a]
        expected = [a, b, c, d, e, f, g]

        organizer = SequenceOrganizer(unsortedList)
        sortedList = organizer.getSortedList()

        self.assertTrue(sortedList == expected)
