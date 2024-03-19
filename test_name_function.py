import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = get_formatted_name('Rajeshkanna', 'Esakkiselvaraj')
		self.assertEqual(formatted_name, 'Rajeshkanna Esakkiselvaraj')
	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name('Rajesh',  'Esakkiselvaraj', 'kanna')
		self.assertEqual(formatted_name, 'Rajesh Kanna Esakkiselvaraj')

if __name__ == '__main__':
	unittest.main()

