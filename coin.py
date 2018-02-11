from __future__ import print_function # Python 2/3 compatibility
import boto3
import urllib, json
import math
import json
import decimal
import datetime
from datetime import timedelta
from datetime import datetime
from datetime import date
from operator import add
from operator import itemgetter
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


# Read peak table to get all coin to review and peak values
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('PeakCoin')
peak_response = table.scan()

market_api = 'https://api.coinmarketcap.com/v1/ticker/?limit=20'
try:
	response = urllib.urlopen(market_api)
	data = json.loads(response.read())
except:
	data = ""

total_market_api = 'https://api.coinmarketcap.com/v1/global/'
try:
	response = urllib.urlopen(total_market_api)
	total_cap_data = json.loads(response.read())
except:
	total_cap_data = ""


#get todays date
today = date.today()
today_ord = today.toordinal()


email_body = ""

#sort coin data from dynamodb
ordered_peak_response = sorted(peak_response['Items'], key=itemgetter('display_order'))

#Coin collections
for i in ordered_peak_response:
	cur_coin = i['coin']
	email_body += str(cur_coin) + "\n"

	if (cur_coin == 'Total_Market_Cap'):
		# total market cap has a different api endpoint
		cur_price = total_cap_data["total_market_cap_usd"]
	else:
		ticker_coin_info = (item for item in data if item['id'] == cur_coin.lower()).next()
		cur_price = ticker_coin_info['price_usd']
	
	peak_price = i['peak_price']
		
	if (float(cur_price) > float(peak_price)):
		#replace peak data item in dynamo
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('PeakCoin')
		table.put_item(
		   Item={
		       'coin': i['coin'],
		       'coin_symbol': i['coin_symbol'],
		       'peak_price': cur_price,
		       'peak_date': str(today),
		       'display_order':i['display_order']
		    }
		)
		email_body += str(cur_price) + "\n"
		email_body += "New peak" + "\n"
		email_body += "\n"
	else:

		cur_date = i['peak_date']
		day_diff = today_ord - datetime.strptime(cur_date, "%Y-%m-%d").toordinal()

		email_body += ("Cur: " + str(cur_price)) + "\n"
		email_body += ("Top: " + str(peak_price)) + "\n"
		email_body += ("%.2f" % (float(cur_price) / float(i['peak_price']) * 100) + "%") + "\n"
		email_body += ("Days since peak: " + str(day_diff)) + "\n"
		email_body += "\n"


msg_client = boto3.client('sns',region_name='us-west-2')
topic = msg_client.create_topic(Name="<INSERT_NAME>")
topic_arn = topic['TopicArn']  # get its Amazon Resource Name
mail_subject = 'Daily Crypto Update: ' + str(today)

print(email_body)


msg_client.publish(TopicArn=topic_arn,Message=email_body,Subject=mail_subject)
