1# -*- coding: utf-8 -*-
"""
02/09/2024
Louie Santino Venegas d41112084 ceis150
"""
from datetime import datetime
from stock_class import Stock, DailyData
from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import csv


def add_stock(stock_list):
      option = ""
      while option != "0":
          print("Add Stock---")
          symbol = input("Enter Ticker Symbol: ")
          symbol = symbol.upper()
          name = input("Enter Company Name: ")
          try:
              shares = float(input("Enter Shares: "))
          except:
              print("Number Values Only!")
          new_stock = Stock(symbol, name, shares)
          stock_list.append(new_stock)
          option = input("Pess Enter to Add Another Stock or 0 to quit: ")

# Remove stock and all daily data
def delete_stock(stock_list):
    print("Delete Stock---")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, " ",end="")
    print("]")
    symbol = input("Which stock do you want to delete?").upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
        i = i + 1
    if found == True:
        print("Deleted", symbol)
    else:
        print("Symbols not found")
        _=input("Press enter to continue")
    
    
    
# List stocks being tracked
def list_stocks(stock_list):
    print("list of Stocks")
    print("SYMBOL\t\tNAME\t\tSHARES")
    print("======================================")
    for stock in stock_list:
        print(stock.symbol," " * (14-len(stock.symbol)),stock.name," " * (14-len(stock.name)),stock.shares)
    print()
    _ = input("Pres enter to continue")
    
    # Add Daily Stock Data
def add_stock_data(stock_list):
    print("Add Daily Stock Data....")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
        
    if found == True:
        print("Ready to add data for: ",symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
                date, price, volume = data.split(",")
                daily_data = DailyData(date,float(price),float(volume))
      
                current_stock.add_data(daily_data)
                data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found...")
        _ = input("Press Enter to Continue...")

    
def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)



# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    date = []
    price = []
    volume = []
    company = ""
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
    plt.plot(date, price)
    plt.xlabel(date)
    plt.ylabel(price)
    plt.title(company)
    plt.show()
    
            
    

# Display Chart
def display_chart(stock_list):
    print("Stock List: [", end='')
    for stock in stock_list:
        print(stock.symbol + " ", end='')
    print("]")
    symbol = input("Enter stock symbol: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            #11current_stock = stock
    if found == True:
        display_stock_chart(stock_list, symbol)
    else:
        print("ERROR: " + symbol + "was not found.")
    _ = input("Press Enter to continue...")
  


                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("Import Stock Data...")
    print("Stock List [", end = '')
    for stock in stock_list:
        print(stock.symbol + " ", end = '')   
    print("]")
    symbol = input("What Symbol Would you like To use: " ).upper()
    fileName = input("Input File Name: ")
    for stock in stock_list:
        if stock.symbol == symbol:
            with open(fileName, newline='') as stockdata:
                datareader= csv.reader(stockdata, delimiter=',')
                next(datareader)
                for row in datareader:
                    daily_data = DailyData(str(row[0]), float(row[4]), float(row[6]))
                    stock.add_data(daily_data)
    display_report(stock_list)
   
    # Display Report 
def display_report(stock_list):
    print("--Stock Report--")
    for stock in stock_list:
        print('\nReport for: ', stock.symbol, stock.name)
        print("Shares: ", stock.shares)
        count = 0 
        price_total = 0 
        volume_total = 0 
        lowPrice = 9999999.99
        highPrice = 0 
        lowVolume = 999999999999
        highVolume = 0
        
        for daily_data in stock.DataList:
            count += 1
            price_total += daily_data.close
            volume_total += daily_data.volume
            if daily_data.close < lowPrice:
                lowPrice = daily_data.close
            if daily_data.close > highPrice:
               highPrice = daily_data.close
            if daily_data.volume < lowVolume:
                lowVolume = daily_data.volume
            if daily_data.volume > highVolume:
                highVolume = daily_data.volume
                
        priceChange = highPrice - lowPrice
        if count > 0:
            print("summary...")
            print("Low Price: ${:,.2f}".format(lowPrice))
            print("High Print: ${:,.2f}".format(highPrice))
            print("Average Price: ${:,.2f}".format(price_total / count))
            print("Low Volume:", highVolume)
            print("Average Volume: {:,.1f}".format(volume_total / count) )
            print("Change in Price: ${:,.2f}".format(priceChange))
            print("profit/loss: ${:,.2f}".format(priceChange * stock.shares))
        else:
            print("No daily history...")
        print("\n\n\n")
    print("Report Complete!")
    _ = input("press enter to contiue")
               
        
        
    
def main_menu(stock_list):
    option = ""
    while True:
        print("\n\nStock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("\nEnter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            
            print("\nError please select from menu...")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()