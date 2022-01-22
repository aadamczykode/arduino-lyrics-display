#include <LiquidCrystal.h>
#include <Firmata.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

char c = '\n';
char e = '^';

void stringDataCallback(char *stringData){
   if (*stringData == c){
    lcd.clear();
   } else if (*stringData == e){
    lcd.noDisplay();
   } else {
    lcd.print(stringData);
   }
}

void setup() {
  lcd.begin(16,2);
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();  
}

void loop() {
  
  while ( Firmata.available() ) {
    Firmata.processInput();
  }
}
