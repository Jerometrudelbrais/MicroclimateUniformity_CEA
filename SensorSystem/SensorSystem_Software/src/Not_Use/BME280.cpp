/*
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include "BME280.h"

#define SEALEVELPRESSURE_HPA (1013.25)
Adafruit_BME280 bme;

void BME280_init(){
  //BME280 test
  Serial.println(F("BME280 test"));
  bool status;
  // default settings
  status = bme.begin(0x77);  
  if (!status) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
  Serial.println("-- Default Test --");
  Serial.println();
}


float BME280_getdata(){
  float Temp;
  Temp = bme.readTemperature(); 
  return Temp;
}
*/