class CurrencyConverter:
    rates = {  
        'EUR': 1.20,  # 1 EUR = 1.20 USD
        'JPY': 0.01   # 1 JPY = 0.01 USD
    } # Class attribute

    # TODO: Implement the static method `to_usd`
    def to_usd(currency, currency_name):
        if currency_name == 'EUR':
            converted = currency * CurrencyConverter.rates[currency_name]
        elif currency_name == "JPY":
            converted = currency * CurrencyConverter.rates[currency_name]
        return converted
    
print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
