#include <SPI.h>
#include <MFRC522.h>
#define SS_PIN 9
#define RST_PIN 8
String x;
String content="";
MFRC522 mfrc522(SS_PIN, RST_PIN); // Instance of the class
void setup() {
   Serial.begin(9600);
   SPI.begin();       // Init SPI bus
   mfrc522.PCD_Init(); // Init MFRC522
   Serial.println("RFID reading UID");
}
void loop(){
  read1();
  Serial.println("c");
  Serial.println(x);
 
}
