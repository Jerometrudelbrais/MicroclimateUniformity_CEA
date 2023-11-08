
/*
#include "Device.h"

#include <Arduino.h>
#include <iostream>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include "Adafruit_VEML7700.h"
#include "Sensor.h"

Adafruit_BME280 bme;
Adafruit_VEML7700 veml = Adafruit_VEML7700();

void Device::update_device(int spec){
    if (spec == 1) {
        data = bme.readTemperature();
    } else if (spec == 2) {
        data = veml.readLux(VEML_LUX_AUTO);
    } 
};
*/