import mysql.connector
from mysql.connector import Error

insuranceConnection = mysql.connector.connect(
		host="brtb9l4ny6wc5d2im2gr-mysql.services.clever-cloud.com",
		user="uhjudei7jpjph6wd",
		passwd="a5UTWKLEYgloWG3w3PU5",
		database="brtb9l4ny6wc5d2im2gr"
	)
insuranceCursor = insuranceConnection.cursor(buffered=True)
