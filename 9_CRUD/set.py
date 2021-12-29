A = {1, 2, 3}    # A set
B = {3, 4, 5}    # B set

A | B     # A U B  { 1 2 3 4 5 }
A & B     # A ∩ B  { 3 }
A - B	  # A - B  { 1 2 }
B - A     # B - A  { 4 5 }


#--------------------------------

# Declare sets
a = set([1, 2, 3]) # it's recommended to use set() because 
a = {1, 2, 3} # this one feels confusing with the dictionaries

a.add(4)