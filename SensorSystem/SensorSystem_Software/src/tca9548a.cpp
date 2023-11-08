#include <Arduino.h>
#include "Wire.h"
#include "tca9548a.h"

#define TCAADDR 0x70

void tca9548a_tcaselect(uint8_t i) {
  if (i > 7) return;
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}


// standard Arduino setup()
void tca9548a_init(){
  Wire.begin();
  Serial.println("\nTCAScanner ready!");
    
  for (uint8_t t=0; t<8; t++) {
    tca9548a_tcaselect(t);
    Serial.print("TCA Port #"); Serial.println(t);

    for (uint8_t addr = 0; addr<=127; addr++) {
      if (addr == TCAADDR) continue;

      Wire.beginTransmission(addr);
      if (!Wire.endTransmission()) {
        Serial.print("Found I2C 0x");  Serial.println(addr,HEX);
      }
    }
  }
  Serial.println("\ndone");
}