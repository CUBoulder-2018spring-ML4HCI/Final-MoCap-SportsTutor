import oscP5.*;
import netP5.*;
import java.util.*;
import java.io.BufferedWriter;
import java.io.FileWriter;

OscP5 oscP5;
OscP5 oscP51;
NetAddress dest;

int KINECT_LOAD = 18;
ArrayList<Float> mb_points = new ArrayList();
ArrayList<Float> kinect_points = new ArrayList();
Stack<ArrayList> kinect_stack = new Stack();
Stack<ArrayList> mb_stack = new Stack();
BufferedWriter output;

String featureString = "";

void setup() {
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this, 6448);
  dest = new NetAddress("localhost", 7000);
}
/* recieves inputs from two programs*/
void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.checkAddrPattern("/wek/inputs/a")==true) {
      if (theOscMessage.checkTypetag("ffffffffffffffffff")) { //Now looking for 2 parameters
        for (int i = 0; i < KINECT_LOAD; i++) {
         kinect_points.add(theOscMessage.get(i).floatValue());
        }
        println("Received new params value from Wekinator");
      } else {
        println("Error: unexpected params type tag received by Processing");
      }
      kinect_stack.push((ArrayList)kinect_points.clone());
  }
  if (theOscMessage.checkAddrPattern("/wek/inputs/b")==true) {
      if (theOscMessage.checkTypetag("ffffff")) { //Now looking for 2 parameters
        for (int i = 0; i < 6; i++) {
          mb_points.add(theOscMessage.get(i).floatValue());
        }
        println("Received new params value from Wekinator");
      } else {
        println("Error: unexpected params type tag received by Processing");
      }
      mb_stack.push((ArrayList)mb_points.clone());
  }
  flushPoints();
}

void flushPoints()
{
  kinect_points.clear();
  mb_points.clear();
}

void draw() {
  if (!(mb_stack.empty()) && !(kinect_stack.empty()))
  {
    sendToPipe(kinect_stack.pop(), mb_stack.pop());
  }
}

/* sends data to wekinator*/
void sendToPipe(ArrayList kinect_points, ArrayList mb_points) {
  try {
    output = new BufferedWriter(new FileWriter("/tmp/un_pipe", true));
  } 
  catch (IOException e) {
    e.printStackTrace();
  }
  StringBuilder sb = new StringBuilder();
  try {
    ArrayList<Float> points = new ArrayList();
    points.addAll(kinect_points);
    points.addAll(mb_points);
    
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