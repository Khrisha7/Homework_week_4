# What is wrong with the above code
# this is a tuple
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
print(cheese)

# Python iterate over the string and adds each character to the string word so we end up 'o', 'k', 'e', rather than a single cheese name 'Oke'.

# How we should add Oke to the cheese name
cheese.append('Oke')
print(cheese)

# how can we add tow new cheeses?
cheese += ['Parmesan', 'Mozzarella']
print(cheese)