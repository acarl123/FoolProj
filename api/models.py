from django.db import models

class Company(models.Model):
    companyName = models.CharField(primary_key=True, max_length=50)
    symbol = models.CharField(max_length=50)
    exchange = models.CharField(max_length=50)
    exchangeName = models.CharField(max_length=50)
    isoAlpha2CountryCode = models.CharField(max_length=50)
    isoAlpha3CountryCode = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    currencyCode = models.CharField(max_length=50)
    instrumentId = models.IntegerField()
    shortInterest = models.IntegerField()
    volume = models.IntegerField()
    sharesOutstanding = models.IntegerField()
    averageVolume = models.IntegerField()
    priceToEarningsRatio = models.FloatField()
    returnOnEquity = models.FloatField()
    lastTradeDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    exDivDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    divPayDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    assetClass = models.IntegerField()
    chartUrl = models.URLField(max_length=200)
    isRealTime = models.BooleanField()
    maturityDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    openInterest = models.IntegerField()
    seoName = models.CharField(max_length=50)
    idcMdgId = models.IntegerField()
    website = models.URLField(max_length=200)
    beta3Y = models.FloatField()
    homeCountryCode = models.CharField(max_length=50, blank=True, null=True)
    grossMargin = models.FloatField()
    revenueGrowth = models.FloatField()

    year1ForwardEPSEstimate = models.ForeignKey("Year1ForwardEPSEstimate", on_delete=models.CASCADE)
    year2ForwardEPSEstimate = models.ForeignKey("Year2ForwardEPSEstimate", on_delete=models.CASCADE)
    change = models.ForeignKey("Change", on_delete=models.CASCADE)
    closePrice = models.ForeignKey("ClosePrice", on_delete=models.CASCADE)
    currentPrice = models.ForeignKey("CurrentPrice", on_delete=models.CASCADE)
    openPrice = models.ForeignKey("OpenPrice", on_delete=models.CASCADE)
    marketCap = models.ForeignKey("MarketCap", on_delete=models.CASCADE)
    marketCapChange = models.ForeignKey("MarketCapChange", on_delete=models.CASCADE)
    earningsPerShare = models.ForeignKey("EarningsPerShare", on_delete=models.CASCADE)
    percentChange = models.ForeignKey("PercentChange", on_delete=models.CASCADE)
    dailyRange = models.ForeignKey("DailyRange", on_delete=models.CASCADE)
    fiftyTwoWeekRange = models.ForeignKey("FiftyTwoWeekRange", on_delete=models.CASCADE)
    annualDividend = models.ForeignKey("AnnualDividend", on_delete=models.CASCADE)
    dividendYield = models.ForeignKey("DividendYield", on_delete=models.CASCADE)
    percentOfSharesTraded = models.ForeignKey("PercentOfSharesTraded", on_delete=models.CASCADE)
    bid = models.ForeignKey("Bid", on_delete=models.CASCADE)
    ask = models.ForeignKey("Ask", on_delete=models.CASCADE)
    askYield = models.ForeignKey("AskYield", on_delete=models.CASCADE)
    bidYield = models.ForeignKey("BidYield", on_delete=models.CASCADE)
    openYield = models.ForeignKey("OpenYield", on_delete=models.CASCADE)
    previousYield = models.ForeignKey("PreviousYield", on_delete=models.CASCADE)


    class Year1ForwardEPSEstimate(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class Year2ForwardEPSEstimate(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class Change(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class ClosePrice(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()

    
    class CurrentPrice(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.models.IntegerField()


    class OpenPrice(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class MarketCap(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class MarketCapChange(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class EarningsPerShare(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class PercentChange(models.Model):
        value = models.FloatField()


    class DailyRange(models.Model):
        minimum = models.ForeignKey("Minimum", on_delete=models.CASCADE)
        maximum = models.ForeignKey("Maximum", on_delete=models.CASCADE)


    class FiftyTwoWeekRange(models.Model):
        minimum = models.ForeignKey("Minimum", on_delete=models.CASCADE)
        maximum = models.ForeignKey("Maximum", on_delete=models.CASCADE)


    class AnnualDividend(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class DividendYield(models.Model):
        value = models.FloatField()


    class PercentOfSharesTraded(models.Model):
        value = models.FloatField()


    class Bid(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class Ask(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.IntegerField()


    class AskYield(models.Model):
        value = models.FloatField()


    class BidYield(models.Model):
        value = models.FloatField()


    class OpenYield(models.Model):
        value = models.FloatField()


    class PreviousYield(models.Model):
        value = models.FloatField()

    class Minimum(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.models.IntegerField()

    class Maximum(models.Model):
        amount = models.CharField(max_length=50)
        currency = models.models.IntegerField()