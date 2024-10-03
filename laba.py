initial_investment = 25000
interest_rate_uah = 11.5 / 100
interest_rate_usd = 4 / 100
exchange_rate_buy = 27
exchange_rate_sell = 28.6

amount_uah = initial_investment * (1 + interest_rate_uah)
amount_usd = (initial_investment / exchange_rate_buy) * (1 + interest_rate_usd) * exchange_rate_sell

if amount_uah > amount_usd:
    print("Вигідніше вкласти в гривнях:", amount_uah)
else:
    print("Вигідніше вкласти в доларах:", amount_usd)
