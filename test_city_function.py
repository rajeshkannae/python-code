import unittest
from city_functions import city_country

class CityTestCases(unittest.TestCase):

	def test_city_country(self):
		formatted_city = city_country('Vikramasingapuram', 'India')
		self.assertEqual(formatted_city, 'Vikramasingapuram, India')
	def test_city_country_population(self):
		formatted_city = city_country('Vikramasingapuram', 'India', 50000)
		self.assertEqual(formatted_city, 'Vikramasingapuram, India - Population 50000')

if __name__ == '__main__':
	unittest.main()

