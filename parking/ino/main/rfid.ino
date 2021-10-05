void read1(){
  if ( mfrc522.PICC_IsNewCardPresent())
    {
        if ( mfrc522.PICC_ReadCardSerial())
        {
           Serial.print("Tag UID:");
           for (byte i = 0; i < mfrc522.uid.size; i++) {
                  Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
                  Serial.print(mfrc522.uid.uidByte[i], HEX);
                  content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
                  content.concat(String(mfrc522.uid.uidByte[i], HEX));
                  x = content.substring(1);
            }
         
            mfrc522.PICC_HaltA();
            return x;
        }
    }
  
}
