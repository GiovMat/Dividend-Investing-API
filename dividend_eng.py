from yahooquery import Ticker

class Stock():
    def __init__(self, symbol):
        ticker = Ticker(symbol)

        self.symbol = symbol
        self.name = ticker.quote_type[symbol]['longName']
        self.currency = ticker.financial_data[symbol]['financialCurrency']
        self.exchange = ticker.quote_type[symbol]['exchange']
        self.industry = ticker.asset_profile[symbol]['industry']
        self.sector = ticker.asset_profile[symbol]['sector']
        self.current_price = ticker.financial_data[symbol]['currentPrice']
        self.dividend_rate = ticker.summary_detail[symbol]['dividendRate'] #! se non ci sono dividendi da errore
        self.eps = ticker.key_stats[symbol]['trailingEps']
        self.core_growth=''
        self.roe = ''

        print(ticker.esg_scores)

stock = Stock('aapl')
print(stock.name, stock.symbol, stock.exchange, stock.currency, stock.industry, stock.sector, stock.current_price, stock.dividend_rate, stock.eps)

# TODO il growth rate lo imposta l'utente? Come calcolarlo in alternativa?