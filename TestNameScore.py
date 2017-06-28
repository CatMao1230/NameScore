import NameScore
import unittest

class TestNameScore(unittest.TestCase):
	def test_access_from_file(self):
		file_name = "NameScore.dat"
		expacted_value = ['ABC', 'CDEF', 'FIJK']
		value = NameScore.access_from_file(file_name)
		self.assertEqual(expacted_value, value)
	def test_name_score(self):
		ls = ['ABC', 'CDEF', 'FIJK']
		expacted_value = [6, 36, 108]
		value = NameScore.name_score(ls)
		self.assertEqual(expacted_value, value)

if __name__ == '__main__':
	unittest.main()
