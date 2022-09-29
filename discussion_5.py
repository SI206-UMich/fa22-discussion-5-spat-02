import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = -1
		for item in self.items:
			if(item.stock > max_stock):
				max_stock = item.stock
				max = item
		return max


	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a(""), 0, "count_a() on empty string")
		self.assertEqual(count_a("aAa"), 2, "count_a() on 'aAa'")
		self.assertEqual(count_a("test sentence without"), 0, "count_a() on 'test sentence without'")
		self.assertEqual(count_a("anaconda and python"), 4, "count_a() on 'anaconda and python'")
		self.assertEqual(count_a("Python and Anaconda"), 3, "count_a() on 'Python and Anaconda'")
		


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		w1 = Warehouse()
		self.assertEqual(len(w1.items), 0, "num items in warehouse before add")

		w1.add_item(self.item1)
		self.assertEqual(len(w1.items), 1, "num items in warehouse after add")
		self.assertEqual(w1.items[0], self.item1, "test if correctly adds item1")

		w1.add_item(self.item2)
		self.assertEqual(len(w1.items), 2, "num items in warehouse after 2nd add")
		self.assertEqual(w1.items[1], self.item2, "test if correctly adds item2")

		w1.add_item(self.item2)
		self.assertEqual(len(w1.items), 3, "num items in warehouse after 2nd repeat add")
		self.assertEqual(w1.items[2], self.item2, "test if correctly re-adds item2")



	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		w1 = Warehouse()
		w1.add_item(self.item1)
		self.assertEqual(w1.get_max_stock(), self.item1, "test get_max_stock with 1 item")

		w1.add_item(Item("Empty box", 1, 21))
		w1.add_item(self.item2)
		self.assertEqual(w1.get_max_stock(), self.item2, "test get_max_stock with 3 items")

		w1.add_item(Item("Juice", 1, 10))
		self.assertEqual(w1.get_max_stock(), self.item2, "test get_max_stock with 4 items")

		w1.add_item(self.item3)
		self.assertEqual(w1.get_max_stock(), self.item3, "test get_max_stock with 5 items")

		w1.add_item(self.item4)
		w1.add_item(self.item5)
		self.assertEqual(w1.get_max_stock(), self.item3, "test get_max_stock with 7 items")



	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()