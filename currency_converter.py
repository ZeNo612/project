
def currency_converter(amount, from_currency, to_currency):
    
    conversion_rate = {
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
    'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # Return 0.0 if the input amount is negative
    if amount < 0:
        return 0.0

    # If the source and target currencies are the same, return the amount unchanged
    if from_currency == to_currency:
        return round(amount, 2)

    # Perform the conversion using the conversion rates dictionary
    if from_currency in conversion_rate and to_currency in conversion_rate[from_currency]:
        converted_amount = amount * conversion_rate[from_currency][to_currency]
        return round(converted_amount, 2)

    # If the conversion is not possible, return 0.0
    return 0.0

if __name__ == "__main__":
    # Take inputs from the user
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency (GBP, CNY, PHP, INR): ")
    to_currency = input("Enter the target currency (GBP, CNY, PHP, INR): ")

    # Call the currency converter function
    converted_amount = currency_converter(amount, from_currency, to_currency)

    # Display the result
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")


# Submit only this file currency_converter.py with the completed function.
# Do not add additional code for calling the function, or code to get user input.