#define trigPin 9
#define echoPin 10

#define redPin 3
#define greenPin 5
#define bluePin 6

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  
    // CLOSE → RED
    analogWrite(redPin, 80);
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 0);
  }
  else if (distance > 10 && distance <= 20) {
    
    analogWrite(redPin, 0);
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 80);
  }
  else {
    // FAR → GREEN
    analogWrite(redPin, 0);
    analogWrite(greenPin, 80);
    analogWrite(bluePin, 0);
  }

  delay(100);
}



