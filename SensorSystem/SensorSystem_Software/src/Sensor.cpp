#include "Sensor.h"

//Initialisation for DS18B20
const int oneWireBus = 2;     
OneWire oneWire(oneWireBus); 
DallasTemperature ds18b20(&oneWire);
int numberOfDevices;
DeviceAddress tempDeviceAddress;
//Initialisation for BME280
#define SEALEVELPRESSURE_HPA (1013.25)
Adafruit_BME680 bme1;
Adafruit_BME680 bme2;
Adafruit_BME680 bme3;
//Initialisation for VEML7700
Adafruit_VEML7700 veml = Adafruit_VEML7700();
//Initialisation for K30
K30 k30 = K30(0x68);
//Initialisation for CCS811
Adafruit_CCS811 ccs1;
Adafruit_CCS811 ccs2;

//Function to get sensor status
bool Sensor::get_status(int type, int I2C_position, uint8_t OneWire_position[8]){
    Serial.println(F("Sensor test"));
    bool status = 0;
    if (type == 1) {
      tca9548a_tcaselect(I2C_position);
      status = bme1.begin(0x77);
      bme1.setHumidityOversampling(BME680_OS_8X);
      bme1.setTemperatureOversampling(BME680_OS_8X);
    } else if (type == 2) {
      status = 1;
    } else if (type == 3) {
      tca9548a_tcaselect(I2C_position);
      status = ccs1.begin();
    }  else if (type == 4) {
      tca9548a_tcaselect(I2C_position);
      status = bme2.begin(0x77);
      bme2.setHumidityOversampling(BME680_OS_8X);
      bme2.setTemperatureOversampling(BME680_OS_8X);
    } else if (type == 5) {
      status = 1;
    } else if (type == 6) {
      tca9548a_tcaselect(I2C_position);
      status = ccs2.begin();
    } else if (type == 7) {
      tca9548a_tcaselect(I2C_position);
      status = bme3.begin(0x77);
      bme3.setHumidityOversampling(BME680_OS_8X);
      bme3.setTemperatureOversampling(BME680_OS_8X);
    } else if (type == 8) {
      status = 1;
    } else if (type == 9) {
      tca9548a_tcaselect(I2C_position);
      float reading;
      status = k30.readCO2(reading);
    }

    if (!status) {
      Serial.println("Could not find a valid sensor, check wiring!");
      while (1);
    }
    Serial.println("Sensor connected");
    Serial.println();
    return status;
}

//Function to get sensor data
float Sensor::get_data(int type, int I2C_position, uint8_t OneWire_position[8]){
    float reading = 0;
    if (type == 1) {
      tca9548a_tcaselect(I2C_position);
      bme1.performReading();
      reading = bme1.temperature;
    } else if (type == 2) {
      reading = bme1.humidity;
    } else if (type == 3) {
      tca9548a_tcaselect(I2C_position);
      ccs1.readData();
      reading = ccs1.geteCO2();
    } else if (type == 4) {
      tca9548a_tcaselect(I2C_position);
      bme2.performReading();
      reading = bme2.temperature;
    } else if (type == 5) {
      reading = bme2.humidity;
    } else if (type == 6) {
      tca9548a_tcaselect(I2C_position);
      ccs2.readData();
      reading = ccs2.geteCO2();
    } else if (type == 7) {
      tca9548a_tcaselect(I2C_position);
      bme3.performReading();
      reading = bme3.temperature;
    } else if (type == 8) {
      reading = bme3.humidity;
    } else if (type == 9) {
      tca9548a_tcaselect(I2C_position);
      k30.readCO2(reading);
    }
    return reading;
}

void Sensor::update_data(Device Data[]){
  for (int i = 0; i < 9; i++){
    Data[i].data  = get_data(Data[i].type, Data[i].I2C_position, Data[i].OneWire_position);
    Serial.println(Data[i].model.c_str());
    Serial.println(Data[i].data);
    delay(250);
  };
}

void Sensor::update_status(Device Data[]){
  for (int i = 0; i < 9; i++){
    Serial.print(i);
    Data[i].status  = get_status(Data[i].type, Data[i].I2C_position, Data[i].OneWire_position);
  };
}

void Sensor::printAddress(DeviceAddress deviceAddress) {
  for (uint8_t i = 0; i < 7; i++){
    if (deviceAddress[i] < 16) Serial.print("0");
      Serial.print(deviceAddress[i], HEX);
  }
}

void Sensor::ds18b20_init() {
  ds18b20.begin();
    // Grab a count of devices on the wire
  numberOfDevices = ds18b20.getDeviceCount();
  
  // locate devices on the bus
  Serial.print("Locating devices...");
  Serial.print("Found ");
  Serial.print(numberOfDevices, DEC);
  Serial.println(" devices.");

  // Loop through each device, print out address
  for(int i=0;i<numberOfDevices; i++){
    // Search the wire for address
    if(ds18b20.getAddress(tempDeviceAddress, i)){
      Serial.print("Found device ");
      Serial.print(i, DEC);
      Serial.print(" with address: ");
      printAddress(tempDeviceAddress);
      Serial.println();
    } else {
      Serial.print("Found ghost device at ");
      Serial.print(i, DEC);
      Serial.print(" but could not detect address. Check power and cabling");
    }
  }
}