import mysql.connector
from mysql.connector import Error

restaurantConnection = mysql.connector.connect(
		host="b6ozuvhquh16mibwxlqc-mysql.services.clever-cloud.com",
		user="up7wlunkxcruzlb2",
		passwd="mB9DEDRo2fTIQpua0pfD",
		database="b6ozuvhquh16mibwxlqc"
	)
restaurantCursor = restaurantConnection.cursor(buffered=True)

