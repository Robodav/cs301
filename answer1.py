def answer1(data, n):
	nums = []
	numCount = {}
	for num in data:
		nums.append(num)
		if num not in numCount:
			numCount[num] = 1
		else:
			numCount[num] += 1
		if numCount[num] > n:
			for i in range(n+1):
				nums.remove(num)
	return nums

print(answer1([5,10,15,10,7,15,10], 2))