import mysql.connector
from mysql.connector import Error

hospitalConnection = mysql.connector.connect(
		host="b4z9hbgia8mxlyqzt4dp-mysql.services.clever-cloud.com",
		user="uzvnijlymworeflo",
		passwd="qn5HytPoZWdFnDuDjQGB",
		database="b4z9hbgia8mxlyqzt4dp"
	)
hospitalCursor = hospitalConnection.cursor(buffered=True)

