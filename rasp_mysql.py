import serial
from xbee import XBee
import mysql.connector

ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = XBee(ser)

db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

while True:
  try:
    response = xbee.wait_read_frame()
    humidity, temperature, wind_speed = response['rf_data']
    
    # store the received data in the database
    cursor = db.cursor()
    sql = "INSERT INTO sensor_data (humidity, temperature, wind_speed) VALUES (%s, %s, %s)"
    val = (humidity, temperature, wind_speed)
    cursor.execute(sql, val)
    db.commit()
    
    # check if 24 hours have passed
    # if yes, calculate the average and send it to the database
    # reset the timer
    
  except KeyboardInterrupt:
    break

ser.close()
