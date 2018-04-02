import netP5.*;
import oscP5.*;

OscP5 oscP5;
NetAddress dest;

float class1 = 0.0;
float class2 = 0.0;
float class3 = 0.0;


void setup() {  
  size(640, 360);
  background(0);
  oscP5 = new OscP5(this, 12000);
}

void draw(){
  background(0);
 
  text("Class 1: " + str(class1), 100, 100);
  text("Class 2: " + str(class2), 100, 150);
  text("Class 3: " + str(class3), 100, 200);
  if (class1 < class2 && class1 < class3){
   text("MIN IS CLASS1", 100, 250); 
  }else if(class2 < class1 && class2 < class3){
   text("MIN IS CLASS2", 100, 250); 
  }else{
   text("MIN IS CLASS3", 100, 250); 
  }
}

void oscEvent(OscMessage theOscMessage) {
 if (theOscMessage.checkAddrPattern("/wek/outputs") == true) {
   class1 = theOscMessage.get(0).floatValue();
   class2 = theOscMessage.get(1).floatValue();
   class3 = theOscMessage.get(2).floatValue();
   
 } 
}

