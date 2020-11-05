# crypto_monitor

Simple crypto price monitoring tool

### Summary
A simple script that utilizes a free crypto price API, to check the market price of various crypto currencies, and also compare them to their peak value.

### Operations
It consists of a dynamoDB table to store the list of coins, as well as the peak price/date. Then the actual script is run as a lambda function on schedule, and 
uses AWS SNS to send an email with the generated html results. SNS is used instead of SES for simplicity sake
