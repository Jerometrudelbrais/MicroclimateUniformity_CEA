#include "Influxdb.h"

InfluxDBClient client(INFLUXDB_URL, INFLUXDB_ORG, INFLUXDB_BUCKET, INFLUXDB_TOKEN, InfluxDbCloud2CACert);
Point InfluxData("Sys1");
ESP8266WiFiMulti wifiMulti;

void Influxdb::wifi_setup(){
    // Setup wifi
    WiFi.mode(WIFI_STA);
    wifiMulti.addAP(WIFI_SSID, WIFI_PASSWORD);

    Serial.print("Connecting to wifi");
    while (wifiMulti.run() != WL_CONNECTED) {
        Serial.print(".");
        delay(100);
    }
    Serial.println();
}

void Influxdb::server_setup(){
    timeSync(TZ_INFO, "ca.pool.ntp.org", "time.nis.gov");
    // Check server connection
    client.setWriteOptions(WriteOptions().writePrecision(WritePrecision::MS));
    if (client.validateConnection()) {
        Serial.print("Connected to InfluxDB: ");
        Serial.println(client.getServerUrl());
    } else {
        Serial.print("InfluxDB connection failed: ");
        Serial.println(client.getLastErrorMessage());
    }
}

void Influxdb::server_update(){
    if (wifiMulti.run() != WL_CONNECTED)                               
        Serial.println("Wifi connection lost");

    if (!client.writePoint(InfluxData))                                   
    {
        Serial.print("InfluxDB write failed: ");
        Serial.println(client.getLastErrorMessage());
    }
}

void Influxdb::data_update(Device Data[]){
    for (int i = 0; i < 9; i++){
        String Timestamp = InfluxData.getTime(); //to solve problem with timestamp 1/2 
        InfluxData.clearFields();
        InfluxData.setTime(Timestamp); //to solve problem with timestamp 1/2 
        InfluxData.clearTags();
        InfluxData.addTag("device", DEVICE);
        const char * a = Data[i].EnvironmentalCondition.c_str(); InfluxData.addTag("Environmental Condition", a);
        const char * c = Data[i].model.c_str();
        InfluxData.addField(c, Data[i].data);
        delay(200);
        server_update();
        Serial.print(i);
    };
}

void Influxdb::TimeStamp(){
    InfluxData.setTime(WritePrecision::MS);
    Serial.print(InfluxData.getTime());
}
