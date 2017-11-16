principal = 10000 #base amount of money
compound = 12 # times it is compounded per year
rate = 0.08 # interest rate
year = input("Enter the amound of years the principal will lie: ") # get years
interest = compound *int(year) # generate interest number
growth = 1 + (rate / compound) # continued
factor = growth ** interest    # continued
returns = principal * factor #calculate the return
print(returns) #output it

