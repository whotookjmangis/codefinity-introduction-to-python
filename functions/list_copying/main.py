# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    prices_copy = product_prices.copy()
    for item in range(len(prices_copy)):
        prices_copy2 = prices.copy()
        if prices_copy2[item] > 2.00:
            prices_copy2[item] *= 0.90
        
        return prices_copy2
    

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(F"Updated product prices: ${updated_prices}")
