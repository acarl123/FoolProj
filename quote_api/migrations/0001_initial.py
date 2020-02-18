# Generated by Django 3.0.3 on 2020-02-17 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualDividend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AskYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BidYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClosePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CurrentPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DividendYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EarningsPerShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MarketCap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MarketCapChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maximum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Minimum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OpenPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OpenYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PercentChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PercentOfSharesTraded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PreviousYield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Year1ForwardEPSEstimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Year2ForwardEPSEstimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('currency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FiftyTwoWeekRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Maximum')),
                ('minimum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Minimum')),
            ],
        ),
        migrations.CreateModel(
            name='DailyRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Maximum')),
                ('minimum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Minimum')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=50)),
                ('exchange', models.CharField(max_length=50)),
                ('exchangeName', models.CharField(max_length=50)),
                ('isoAlpha2CountryCode', models.CharField(max_length=50)),
                ('isoAlpha3CountryCode', models.CharField(max_length=50)),
                ('sector', models.CharField(blank=True, max_length=50, null=True)),
                ('industry', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=250)),
                ('currencyCode', models.CharField(max_length=50)),
                ('instrumentId', models.IntegerField()),
                ('shortInterest', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('sharesOutstanding', models.IntegerField()),
                ('averageVolume', models.IntegerField()),
                ('priceToEarningsRatio', models.FloatField()),
                ('returnOnEquity', models.FloatField()),
                ('lastTradeDate', models.DateTimeField()),
                ('exDivDate', models.DateTimeField()),
                ('divPayDate', models.DateTimeField()),
                ('assetClass', models.IntegerField()),
                ('chartUrl', models.URLField(blank=True, null=True)),
                ('isRealTime', models.BooleanField()),
                ('maturityDate', models.DateTimeField()),
                ('openInterest', models.IntegerField()),
                ('seoName', models.CharField(max_length=50)),
                ('idcMdgId', models.IntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('beta3Y', models.FloatField()),
                ('homeCountryCode', models.CharField(blank=True, max_length=50, null=True)),
                ('grossMargin', models.FloatField()),
                ('revenueGrowth', models.FloatField()),
                ('annualDividend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.AnnualDividend')),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Ask')),
                ('askYield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.AskYield')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Bid')),
                ('bidYield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.BidYield')),
                ('change', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Change')),
                ('closePrice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.ClosePrice')),
                ('currentPrice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.CurrentPrice')),
                ('dailyRange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.DailyRange')),
                ('dividendYield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.DividendYield')),
                ('earningsPerShare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.EarningsPerShare')),
                ('fiftyTwoWeekRange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.FiftyTwoWeekRange')),
                ('marketCap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.MarketCap')),
                ('marketCapChange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.MarketCapChange')),
                ('openPrice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.OpenPrice')),
                ('openYield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.OpenYield')),
                ('percentChange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.PercentChange')),
                ('percentOfSharesTraded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.PercentOfSharesTraded')),
                ('previousYield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.PreviousYield')),
                ('year1ForwardEPSEstimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Year1ForwardEPSEstimate')),
                ('year2ForwardEPSEstimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_api.Year2ForwardEPSEstimate')),
            ],
        ),
    ]