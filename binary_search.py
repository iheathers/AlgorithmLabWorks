def binary_search(arr,num):
	firstIndex = 0
	lastIndex = len(array)-1
	found = False

	while firstIndex <= lastIndex and not found:
		index = int((firstIndex + lastIndex)/2)

		if array[index] == num:
			found = True
			return index

		else: 
			if num < array[index]:
				lastIndex = index-1

			else:
				firstIndex = index+1

				
