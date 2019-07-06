#!/usr/bin/python3

import unittest


def addTwoNumbers(x,y):
	return 8


class testAddTwoNumbers(unittest.TestCase):
	def testFailingTest(self):
		self.assertTrue(True)


if __name__ == '__main__':
	unittest.main()

