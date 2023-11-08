#include <Arduino.h>
#include "Device.h"
#include "Sensor.h"
#include "Influxdb.h"


Influxdb InfluxHandler; 
Sensor SensorHandler;

Device   Data[] = {{ "BME680_01", "Temperature",1, 0, 0, 0, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   { "BME680_01",    "Humidity",2, 0, 0, 0, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   { "CCS811_01",         "CO2",3, 0, 0, 0, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   { "BME680_02", "Temperature",4, 0, 0, 1, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   { "BME680_02",    "Humidity",5, 0, 0, 1, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   { "CCS811_02",         "CO2",6, 0, 0, 1, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   { "BME680_03", "Temperature",7, 0, 0, 2, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   { "BME680_03",    "Humidity",8, 0, 0, 2, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}},
                   {     "K30_1",         "CO2",9, 0, 0, 2, {0x28, 0x4B, 0x4D, 0x75, 0xD0, 0x01, 0x3C, 0x7F}}};


void setup() {
  Serial.begin(9600);
  delay(10000);
  InfluxHandler.wifi_setup();
  InfluxHandler.server_setup();
  SensorHandler.update_status(Data);
}

void loop(){
  InfluxHandler.TimeStamp();
  SensorHandler.update_data(Data);
  InfluxHandler.data_update(Data);
  Serial.print("ok");
  delay(10000);
  Serial.println("----------------------------");
};
