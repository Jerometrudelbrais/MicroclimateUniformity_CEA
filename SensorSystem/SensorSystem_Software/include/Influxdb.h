#ifndef Influxdb_h
#define Influxdb_h

#include <InfluxDbClient.h>
#include <InfluxDbCloud.h>
#include "Device.h"

#include <ESP8266WiFiMulti.h>
#define DEVICE "ESP8266"
#define WIFI_SSID "EXKA"
#define WIFI_PASSWORD "JxKeRP19wX89"
#define INFLUXDB_URL "https://us-east-1-1.aws.cloud2.influxdata.com"
#define INFLUXDB_TOKEN "9de8Mi02CspBSd9WkVYaWqammphEqGNuqpffASda-DCxFEuDH9edXYMx1w7x4MUiWWYS6ATlip2KYKtkib0bbg=="
#define INFLUXDB_ORG "jerome.trudel-brais@mail.mcgill.ca"
#define INFLUXDB_BUCKET "Sensor"
#define TZ_INFO "EST5EDT,M3.2.0,M11.1.0"

class Influxdb{
    public:
        void wifi_setup();
        void server_setup();
        void data_update(Device Data[]);
        void server_update();
        void TimeStamp();
};
#endif