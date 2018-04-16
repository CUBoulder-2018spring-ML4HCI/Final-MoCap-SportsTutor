import oscP5.*;
import netP5.*;

OscP5 oscP5;
OscP5 oscP51;
NetAddress dest;


float p1 = 0.5;
float p2 = 0.5;
float p3 = 0.5;
float p4 = 0.5;
float p5 = 0.5;
float p6 = 0.5;
float p7 = 0.5;
float p8 = 0.5;
float p9 = 0.5;
float p10 = 0.5;
float p11 = 0.5;
float p12 = 0.5;
float p13 = 0.5;
float p14 = 0.5;
float p15 = 0.5;
float p16 = 0.5;
float p17 = 0.5;
float p18 = 0.5;

void setup() {
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this,6448);
  dest = new NetAddress("localhost",7000);
}
 /* recieves inputs from two programs*/
void oscEvent(OscMessage theOscMessage) {
 if (theOscMessage.checkAddrPattern("/wek/inputs/a")==true) {
     if(theOscMessage.checkTypetag("ffffffffffff")) { //Now looking for 2 parameters
        p1 = theOscMessage.get(0).floatValue(); //get first parameter
        p2 = theOscMessage.get(1).floatValue(); 
        p3 = theOscMessage.get(2).floatValue(); 
        p4 = theOscMessage.get(3).floatValue(); //get first parameter
        p5 = theOscMessage.get(4).floatValue(); 
        p6 = theOscMessage.get(5).floatValue();
        p7 = theOscMessage.get(6).floatValue(); //get first parameter
        p8 = theOscMessage.get(7).floatValue(); 
        p9 = theOscMessage.get(8).floatValue(); 
        p10 = theOscMessage.get(9).floatValue(); //get first parameter
        p11 = theOscMessage.get(10).floatValue(); 
        p12 = theOscMessage.get(11).floatValue();
        println("Received new params value from Wekinator");  
      } else {
        println("Error: unexpected params type tag received by Processing");
      }
 }
 if (theOscMessage.checkAddrPattern("/wek/inputs/b")==true) {
     if(theOscMessage.checkTypetag("ffffff")) { //Now looking for 2 parameters
       
        p13 = theOscMessage.get(0).floatValue(); //get first parameter
        p14 = theOscMessage.get(1).floatValue(); 
        p15 = theOscMessage.get(2).floatValue();
        p16 = theOscMessage.get(3).floatValue(); //get first parameter
        p17 = theOscMessage.get(4).floatValue(); 
        p18 = theOscMessage.get(5).floatValue(); 

        println("Received new params value from Wekinator");  
      } else {
        println("Error: unexpected params type tag received by Processing");
      }
 }
}
 
void draw() {
   sendOsc();
}
 /* sends data to wekinator*/
void sendOsc() {
  OscMessage msg = new OscMessage("/wek/inputs");
  msg.add(p1); 
  msg.add(p2);
  msg.add(p3);
  msg.add(p4);
  msg.add(p5); 
  msg.add(p6);
  msg.add(p7); 
  msg.add(p8);
  msg.add(p9);
  msg.add(p10);
  msg.add(p11); 
  msg.add(p12);
  msg.add(p13); 
  msg.add(p14);
  msg.add(p15);
  msg.add(p16);
  msg.add(p17); 
  msg.add(p18);
  oscP5.send(msg, dest);

}
