#ifndef Sensor_h
#define Sensor_h

#include <Arduino.h>
#include <iostream>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME680.h>
#include <Adafruit_CCS811.h>
#include "Adafruit_VEML7700.h"
#include <DallasTemperature.h>
#include "K30.h"
#include "tca9548a.h"
#include "Device.h"

class Sensor{
    public:
        bool get_status(int type, int I2C_position, uint8_t OneWire_position[8]);
        float get_data(int type, int I2C_position, uint8_t OneWire_position[8]);
        void printAddress();
        void update_data(Device Data[]);
        void update_status(Device Data[]);
        void printAddress(DeviceAddress deviceAddress);
        void ds18b20_init();
};

#endif
