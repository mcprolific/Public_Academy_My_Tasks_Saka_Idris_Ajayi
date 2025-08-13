#Nigerian Currency Converter (Very Advanced)
#===========================================

#Inputs
amount_naira = float(input("Enter amount in Naira: "))
exchange_usd = float(input("Enter exchange rate to US Dollars: "))
exchange_gbp = float(input("Enter exchange rate to British Pounds: "))

#Conversions
amount_usd = amount_naira * exchange_usd
amount_gbp = amount_naira * exchange_gbp

#Presults in a neat table with alignment using escape sequences
print("\nCurrency Conversion Report")
print("----------------------------")
print(f"{'Currency':<15}{'Amount':>20}")
print("----------------------------")
print(f"{'Naira (N)':<15}N{amount_naira:>19,.2f}")
print(f"{'US Dollars ($)':<15}${amount_usd:>19,.2f}")
print(f"{'British Pounds (£)':<15}£{amount_gbp:>19,.2f}")
print("----------------------------")
