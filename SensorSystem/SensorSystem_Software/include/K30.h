#ifndef K30_h
#define K30_h

#include "Arduino.h"

class K30
{
  public:
    K30(int i2c_address);
    int readCO2(float &CO2level);
  private:
    int _i2c_address;
};


#endif
