def f(x):
	steps = 0
	for i in range(1000): # 1000 steps
		steps += 1
	
	for i in range(x): # x steps
		steps += 1
	
	for i in range(x): # (x * x)2 steps = 2(x^2)
		for j in range(x):
			steps += 1
			steps += 1
	
	return steps # 1000 + x + 2(x^2)
	
