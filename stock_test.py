stocks_from_yesterday = [12, 90, 65, 13, 41, 110, 87, 52, 150, 70]

def deter_max_profit_from_stocks(stocks_from_yesterday):
	profit = 0
	sell = 0
	buy = stocks_from_yesterday[0] # assume that there is at least one stock

	for stock_price in stocks_from_yesterday:
		sell = stock_price
		if sell <= buy: # we have a stock price smaller than current one we are buying
			buy = sell
		else:			# calculate profit
			calculated_profit = sell - buy
			if calculated_profit >= profit:
				profit = calculated_profit

	return profit

def deter_max_profit(stocks_from_yesterday):
	max_profit = 0
	min_price = stocks_from_yesterday[0]

	for current_price in stocks_from_yesterday:
		min_price = min(min_price, current_price)
		max_profit = max(max_profit, current_price - min_price)

	return max_profit
