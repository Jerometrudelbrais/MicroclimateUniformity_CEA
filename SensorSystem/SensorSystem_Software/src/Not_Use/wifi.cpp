/*
#include <Arduino.h>
#include "ESP8266WiFi.h"
#include "wifi.h"

//Wifi and MQTT information
const char* ssid = "EXKA";
const char* password =  "JxKeRP19wX89";

void wifi(){
  //Connecting to WIFI
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.print("Connected to WiFi :");
  Serial.println(WiFi.SSID());
}*/