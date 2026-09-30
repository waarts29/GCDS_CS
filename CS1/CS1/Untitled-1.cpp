/*
Authors: Marciano, Krumlauf
Date: 10/13/2023
Description: Turns an LED on/off based on values from a photoresistor
Bugs: Adjust photoresistor value thresholds based on setting
Challenges: None
Sources: https://www.instructables.com/How-to-use-a-photoresistor-or-photocell-Arduino-Tu/
*/

// Initialization
const int ledPin = 9;          // LED pin at Arduino pin 9
const int pResistor = A0;      // Photoresistor at Arduino analog pin A0
int pResistorValue;            // Store value from photoresistor (0–1023)

// Setup
void setup() {
  pinMode(ledPin, OUTPUT);     // Set LED pin to output
  pinMode(pResistor, INPUT);   // Set photoresistor pin to input
  Serial.begin(9600);          // Set up Serial monitor (9600 baud)
}

// Execution
void loop() {
  pResistorValue = analogRead(pResistor);  // Read photoresistor value
  Serial.println(pResistorValue);           // Print value to Serial Monitor

  if (pResistorValue > 250) {                // Light above threshold
    digitalWrite(ledPin, LOW);               // Turn LED off
  } else {
    digitalWrite(ledPin, HIGH);              // Turn LED on
  }

  delay(500);                                // Small delay (500 ms)