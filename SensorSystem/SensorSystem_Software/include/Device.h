#ifndef Device_h
#define Device_h

#include <iostream>
#include <DallasTemperature.h>

class Device{
    public:
        std::string model;
        std::string EnvironmentalCondition;
        int type;
        bool status;
        float data;
        int I2C_position;
        uint8_t OneWire_position[8];
};

#endif
