import oscP5.*;
import netP5.*;
import java.util.*;
import java.io.BufferedWriter;
import java.io.FileWriter;

OscP5 oscP5;
OscP5 oscP51;
NetAddress dest;

int KINECT_LOAD = 18;
ArrayList<Float> points;
BufferedWriter output;

String featureString = "";

void setup() {
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this, 6448);
  dest = new NetAddress("localhost", 7000);
}
/* recieves inputs from two programs*/
void oscEvent(OscMessage theOscMessage) {
  points = new ArrayList<Float>();
  if (theOscMessage.checkAddrPattern("/wek/inputs/a")==true) {
    if (theOscMessage.checkTypetag("ffffffffffffffffff")) { //Now looking for 2 parameters
      for (int i = 0; i < KINECT_LOAD; i++) {
        points.add(theOscMessage.get(i).floatValue());
      }
      println("Received new params value from Wekinator");
    } else {
      println("Error: unexpected params type tag received by Processing");
    }
  }
  if (theOscMessage.checkAddrPattern("/wek/inputs/b")==true) {
    if (theOscMessage.checkTypetag("ffffff")) { //Now looking for 2 parameters

      for (int i = 0; i < 6; i++) {
        points.add(theOscMessage.get(i).floatValue());
      }

      println("Received new params value from Wekinator");
    } else {
      println("Error: unexpected params type tag received by Processing");
    }
  }
}

void flushPoints()
{
  points.clear();
}

void draw() {
  if (points.size() == KINECT_LOAD + 6)
  {
    sendToPipe();
    flushPoints();
  }
}
/* sends data to wekinator*/
void sendToPipe() {
  try {
    output = new BufferedWriter(new FileWriter("/tmp/un_pipe", true));
  } 
  catch (IOException e) {
    e.printStackTrace();
  }
  StringBuilder sb = new StringBuilder();
  try {
    for (int i = 0; i < points.size(); i++) {
      float f = points.get(i);
      sb.append(String.format("%.2f", f)).append(",");
    }

    featureString = sb.toString();
  } 
  catch (Exception ex) {
    println("Encountered exception parsing string: " + ex);
  }

  try {
    output.write(featureString);
    output.close();
  }
  catch (IOException e) {
    e.printStackTrace();
  }
}