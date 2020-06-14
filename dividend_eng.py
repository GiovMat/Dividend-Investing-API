from yahooquery import Ticker

_hurdle_return = {  1:0.12,
                    2:0.11,
                    3:0.10,
                    4:0.09,
                    5:0.09,
                    6:0.09,
                    7:0.09,
                    8:0.10,
                    9:0.11,
                    10:0.12 }

class Stock():
    def __init__(self, symbol):
        # TODO gestire il caso in cui il simbolo è sbagliato
        ticker = Ticker(symbol)

        self.symbol = symbol
        self.name = ticker.quote_type[symbol]['longName']
        self.currency = ticker.financial_data[symbol]['financialCurrency']
        self.exchange = ticker.quote_type[symbol]['exchange']
        self.industry = ticker.asset_profile[symbol]['industry']
        self.sector = ticker.asset_profile[symbol]['sector']
        self.current_price = ticker.financial_data[symbol]['currentPrice']

        if 'dividendRate' in ticker.summary_detail[symbol]:
            self.dividend_rate = ticker.summary_detail[symbol]['dividendRate']
        else:
            self.dividend_rate = 0

        self.eps = ticker.key_stats[symbol]['trailingEps']
        self.roe = ticker.financial_data[symbol]['returnOnEquity']

        # Calcolo del growth rate sulla base della crescita dei dividendi degli ultimi 5 anni e del core growth stimato
        self.dividends = ticker.cash_flow()['CashDividendsPaid']
        self.dividend_perc_growth = self.dividends.pct_change().dropna().mean()

        # TODO calcolare il core gorwth,per ora usiamo la media dei dividendi negli ultimi 5 anni
        self.core_growth=''

        #! da correggere quando si inserirà il core growth, non tiene conto di rendimenti superiori al 10%
        req_return = _hurdle_return[(self.dividend_perc_growth*100).round()]
        self.present_value = (self.dividend_rate / (req_return - self.dividend_perc_growth)).round()
        self.actual_return = (self.dividend_rate/self.current_price) + self.dividend_perc_growth