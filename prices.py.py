# -*- coding: utf-8 -*-
"""
Louie Venegas 
ceis150
January 5, 2024

"""
count = 0            #initialize the count variable to 0
sum = 0              #initialize the sum variable to 0
Full_name = input ("What is Your Full_Nam:? ")            #input full_name
min_price = float( input("What is the Minimum Price?"))  #input the min_price and convert it to float
price_list = [10, 25.5, 50, 22, 69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]    #create a list of prices example: price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]
for price in price_list:    #add current price to sum
    sum += price
    if price > min_price:
       count += 1
print("Hello",Full_name,"the minimum price is $",min_price)   #output "Hello",name,"the minimum price is ",min_price
print("Hello {}, the minimum price is ${:,.2f}" .format(Full_name, min_price))  #output "There are ",count,"prices greater than the minimum price"
print("There are ",count,"prices greater than the minimum price")
print("The total price is ${:,.2f}".format(sum))     #output "The total price is ",sum
