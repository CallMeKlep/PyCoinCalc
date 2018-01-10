#Ask user to input investment amounts and store values
print("Please input investment amounts for each type of currency")
btc_in = float(input("Bitcoin investment: "))
eth_in = float(input("Ethereum investment: "))
ltc_in = float(input("Litecoin investment: "))
bch_in = float(input("Bitcoin Cash investment: "))

#Calculate total investment
total_in = btc_in + eth_in + ltc_in + bch_in

#Print total investment
print("Your total investment is: ${} ".format(total_in))

#Ask user to input value 