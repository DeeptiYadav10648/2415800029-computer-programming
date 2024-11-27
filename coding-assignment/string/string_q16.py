#16 The Town Market Sale:
price=input()
price1=price.split()
reversed_prices = [price[::-1] for price in price1]
out = ' '.join(reversed_prices)
print(out)
