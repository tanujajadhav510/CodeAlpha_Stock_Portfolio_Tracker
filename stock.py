import csv

def stock_portfolio():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 330,
        "AMZN": 135
    }
    
    # Initial portfolio (already bought stocks)
    initial_portfolio = {
        "AAPL": 5,
        "GOOGL": 2
    }
    
    # Calculate initial total investment
    total_value = sum(stock_prices[s] * q for s, q in initial_portfolio.items())
    
    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"- {stock}: ${price}")
    
    # Show initial portfolio
    print("\n📊 Your Initial Portfolio:")
    for stock, qty in initial_portfolio.items():
        print(f"- {stock}: {qty} shares → ${stock_prices[stock] * qty}")
    print(f"💰 Total Investment so far: ${total_value}")
    
    # Start user input
    portfolio = initial_portfolio.copy()
    
    while True:
        stock = input("\nEnter stock symbol to buy (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not available in list.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        investment = stock_prices[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_value += investment
        
        print(f"✅ Added {quantity} shares of {stock}. Investment: ${investment}")
    
    # Display final portfolio
    print("\n📊 Final Portfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"- {stock}: {qty} shares → ${stock_prices[stock] * qty}")
    print(f"\n💰 Total Investment Value: ${total_value}")
    
    # Save to file
    save_choice = input("\nDo you want to save the result? (y/n): ").lower()
    if save_choice == "y":
        file_type = input("Save as TXT or CSV? (txt/csv): ").lower()
        
        if file_type == "txt":
            with open("portfolio.txt", "w") as f:
                f.write("Portfolio Summary:\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
                f.write(f"\nTotal Investment: ${total_value}\n")
            print("📂 Saved to portfolio.txt")
        
        elif file_type == "csv":
            with open("portfolio.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Value"])
                for stock, qty in portfolio.items():
                    writer.writerow([stock, qty, stock_prices[stock] * qty])
                writer.writerow(["TOTAL", "", total_value])
            print("📂 Saved to portfolio.csv")
        else:
            print("⚠️ Invalid file type. Skipping save.")

if __name__ == "__main__":
    stock_portfolio()
