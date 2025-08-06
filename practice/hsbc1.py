a = [-11,2,19,37,64,-18]

m = len(a)
b = 3

def orderPizza(orderPlaced, size):
	# Write your code here

	m = len(orderPlaced)
	n = size
	final = []

	for i in range((m - n) + 1):

		currentOrder = orderPlaced[i:i+n]
		count = 0
		for order in currentOrder:

			if order < 0:
				final.append(order)
				break
			
	return final


result = orderPizza(a, b)

