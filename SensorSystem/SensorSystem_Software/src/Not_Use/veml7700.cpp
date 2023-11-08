/*
#include <Arduino.h>
#include "Adafruit_VEML7700.h"
#include "veml7700.h"

Adafruit_VEML7700 veml = Adafruit_VEML7700();

void veml7700_init(){
    Serial.println("Adafruit VEML7700 Auto Lux Test");

    if (!veml.begin()) {
    Serial.println("Sensor not found");
    while (1);
    }
    Serial.println("Sensor found");

};

float veml7700_getdata(){
    float lux = veml.readLux(VEML_LUX_AUTO);
    return lux;
};
*/

