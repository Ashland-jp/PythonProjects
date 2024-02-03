import requests

# define a function to convert currency
def currency_converter(amount, from_currency, to_currency):
    # set API endpoint for conversion
    api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"


    # send GET request to api
    response = requests.get(api_endpoint)

    # get JSON data from response
    data = response.json()

    # extract exchange rate for target currency
    exchange_rate = data["rates"][to_currency]

    # calculate the converted amount
    converted_amount = amount * exchange_rate

    # return the converted amount

    return converted_amount

# prompt user to enter the amount, source currency, and target currency
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency code: ").upper()
to_currency = input("Enter the target currency code: ").upper()

# convert the currency and print results

result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")