import NameScore
import unittest

class TestNameScore(unittest.TestCase):
	def test_access_from_file(self):
		file_name = "NameScore.dat"
		expacted_value = ['ABC', 'CDEF', 'FIJK']
		value = NameScore.access_from_file(file_name)
		self.assertEqual(expacted_value, value)
	def test_fix_str_1(self):
		ls = '"aB C","CD***EF","FI JK"'
		expacted_value = ['ABC', 'CDEF', 'FIJK']
		value = NameScore.fix_str(ls)
		self.assertEqual(expacted_value, value)
	def test_fix_str_2(self):
		ls = '"98YA--","     ","\\\\!!!O"'
		expacted_value = ['YA', '', 'O']
		value = NameScore.fix_str(ls)
		self.assertEqual(expacted_value, value)
	def test_name_score_1(self):
		ls = ['ABC', 'CDEF', 'FIJK']
		expacted_value = [6, 36, 108]
		value = NameScore.name_score(ls)
		self.assertEqual(expacted_value, value)
	def test_name_score_2(self):
		ls = ['A', 'CD', '']
		expacted_value = [1, 14, 0]
		value = NameScore.name_score(ls)
		self.assertEqual(expacted_value, value)

if __name__ == '__main__':
	unittest.main()
