from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('PeakCoin')

table.put_item(
   Item={
       'coin': 'Bitcoin',
       'coin_symbol': 'BTC',
       'peak_price': '19629',
       'peak_date': '2017-12-17',
       'display_order': 1,
    }
)

table.put_item(
   Item={
       'coin': 'Ethereum',
       'coin_symbol': 'ETH',
       'peak_price': '1419',
       'peak_date': '2018-01-13',
       'display_order': 2,
    }
)

table.put_item(
   Item={
       'coin': 'Ripple',
       'coin_symbol': 'XRP',
       'peak_price': '3.82',
       'peak_date': '2018-01-04',
       'display_order': 3,
    }
)

table.put_item(
   Item={
       'coin': 'Bitcoin-Cash',
       'coin_symbol': 'BCH',
       'peak_price': '4300.04',
       'peak_date': '2017-12-20',
       'display_order': 4,
    }
)

table.put_item(
   Item={
       'coin': 'Cardano',
       'coin_symbol': 'ADA',
       'peak_price': '1.32',
       'peak_date': '2018-01-04',
       'display_order': 5,
    }
)

table.put_item(
   Item={
       'coin': 'Stellar',
       'coin_symbol': 'XLM',
       'peak_price': '0.938144',
       'peak_date': '2018-01-04',
       'display_order': 6,
    }
)

table.put_item(
   Item={
       'coin': 'Nem',
       'coin_symbol': 'XEM',
       'peak_price': '2.09',
       'peak_date': '2018-01-04',
       'display_order': 7,
    }
)

table.put_item(
   Item={
       'coin': 'Litecoin',
       'coin_symbol': 'LTC',
       'peak_price': '365.47',
       'peak_date': '2017-12-19',
       'display_order': 8,
    }
)

table.put_item(
   Item={
       'coin': 'Neo',
       'coin_symbol': 'NEO',
       'peak_price': '192.26',
       'peak_date': '2018-01-15',
       'display_order': 9,
    }
)

table.put_item(
   Item={
       'coin': 'EOS',
       'coin_symbol': 'EOS',
       'peak_price': '18.71',
       'peak_date': '2018-01-13',
       'display_order': 10,
    }
)

table.put_item(
   Item={
       'coin': 'Tron',
       'coin_symbol': 'TRX',
       'peak_price': '0.287933',
       'peak_date': '2018-01-05',
       'display_order': 11,
    }
)

table.put_item(
   Item={
       'coin': 'Total_Market_Cap',
       'coin_symbol': 'TMC',
       'peak_price': '830742000000',
       'peak_date': '2018-01-17',
       'display_order': 0,
    }
)