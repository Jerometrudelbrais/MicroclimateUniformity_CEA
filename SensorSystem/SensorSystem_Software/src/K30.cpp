#include "Arduino.h"
#include "K30.h" 
#include "Wire.h"


K30::K30(int i2c_address){

  _i2c_address = i2c_address;
  Wire.begin();
}

int K30::readCO2(float &CO2level)
{
  
  byte recValue[4] = {0,0,0,0};
  

  Wire.beginTransmission(_i2c_address);
  Wire.write(0x22);
  Wire.write(0x00);
  Wire.write(0x08);
  Wire.write(0x2A);
  Wire.endTransmission();
  delay(30); 
  

  Wire.requestFrom(_i2c_address,4);
  delay(20);
   
  byte i=0;
  while(Wire.available())
  {
    recValue[i] = Wire.read();
    i++;
  }
  
  byte checkSum = recValue[0] + recValue[1] + recValue[2];
  CO2level = (recValue[1] << 8) + recValue[2];
  
  if (i == 0){
    return 0;
  }
  else if(checkSum == recValue[3]){
    return 1;
  }
  else{
    return 0;
  }

}
