import mysql.connector
from mysql.connector import Error

healthCareConnection = mysql.connector.connect(
		host="bbmxoe6jlcdae5p5cusv-mysql.services.clever-cloud.com",
		user="u7iilamfbupfinv2",
		passwd="fg4Kd6aJ7aGcD5kQYxUa",
		database="bbmxoe6jlcdae5p5cusv"
	)
healthCareCursor = healthCareConnection.cursor(buffered=True)

