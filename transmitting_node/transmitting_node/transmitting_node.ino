#include <DHT.h>
#include <SoftwareSerial.h>
#include <XBee.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

SoftwareSerial XBeeSerial(10, 11);
XBee xbee = XBee();

void setup() {
  dht.begin();
  XBeeSerial.begin(9600);
  xbee.setSerial(XBeeSerial);
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  float wind_speed = // read wind speed from Davies Anemometer sensor
  
  // create the data packet to be sent
  uint8_t payload[] = {humidity, temperature, wind_speed};
  Tx16Request tx = Tx16Request(0xFFFF, payload, sizeof(payload));
  
  // send the data packet via XBee
  xbee.send(tx);
  
  delay(300000); // wait for 5 minutes
}
