stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400
}

stock_name = input("Enter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))

if stock_name in stock_prices:
    total = stock_prices[stock_name] * quantity

    print("\n----- Portfolio Summary -----")
    print("Stock:", stock_name)
    print("Quantity:", quantity)
    print("Total Investment Value: $", total)

    with open("portfolio.txt", "w") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: ${total}")

    print("\nData saved in portfolio.txt")

else:
    print("Stock Not Found!")