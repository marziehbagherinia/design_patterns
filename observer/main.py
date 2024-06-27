from colorama import init, Fore, Style
from models.Strategies.Strategy import *
from models.Dashboards.Dashboard import *
from models.StockManagers.StockManager import *

# Initialize colorama
init()

if __name__ == "__main__":
    # Create subject
    stockManager = StockManager()

    # Add stock to subject
    stockManager.set_stock_price("AAPL", 150.00)
    stockManager.set_stock_price("GOOGL", 2800.00)

    # Create observers
    dashboard = Dashboard()
    rsi_strategy = Strategy("RSI")
    macd_strategy = Strategy("MACD")

    # Register observers
    stockManager.register(rsi_strategy)
    stockManager.register(macd_strategy)
    stockManager.register(dashboard)

    # Print obervers init data
    print(Fore.RED + "Observers init data" + Style.RESET_ALL)
    dashboard.print()
    rsi_strategy.print()
    macd_strategy.print()

    # Change stock prices
    stockManager.set_stock_price("GOOGL", 2800.00)
    stockManager.set_stock_price("AAPL", 155.00)

    # Print obervers updated data
    print(Fore.RED + "Observers updated data" + Style.RESET_ALL)
    dashboard.print()
    rsi_strategy.print()
    macd_strategy.print()