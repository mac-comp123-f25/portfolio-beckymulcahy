def add_tax(price, tax_rate):
    print('price and tax rate inputs:', price, tax_rate)
    tax_amt = price * tax_rate
    print(tax_amt, 'return value:', tax_amt)
    return price + tax_amt

add_tax(25.99, 0.0725)

'''Local Environment 
tax_amt = 25.99 * 0.0725
'''

