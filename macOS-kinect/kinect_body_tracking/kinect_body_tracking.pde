import SimpleOpenNI.*;
import netP5.*;
import oscP5.*;

SimpleOpenNI kinect;
OscP5 oscP5;
NetAddress dest;

void setup() {
  size(640, 480);
  kinect = new SimpleOpenNI(this);
  oscP5 = new OscP5(this, 1200);
  dest = new NetAddress("localhost", 6448);
  kinect.enableDepth();
  // turn on user tracking
  kinect.enableUser();
}

// We should use the confidence to get more accurate data, but for MVP
// we will not
// Best interval = 0.5
PVector getDot(int userId, int SimpleJoint) {
  PVector joint = new PVector();
  float confidence = kinect.getJointPositionSkeleton(userId, SimpleJoint, joint);
  PVector convertedJoint = new PVector();
  kinect.convertRealWorldToProjective(joint, convertedJoint);
  return convertedJoint;
}

void draw() {
  kinect.update();
  PImage depth = kinect.depthImage();
  image(depth, 0, 0);
  OscMessage msg = new OscMessage("/wek/inputs");
  // make a vector of ints to store the list of users
  IntVector userList = new IntVector();
  // write the list of detected users
  // into our vector
  kinect.getUsers(userList);
  // if we found any users
  if (userList.size() > 0) {
    // get the first user
    int userId = userList.get(0);
    // if we’re successfully calibrated
    if ( kinect.isTrackingSkeleton(userId)) {
      int all = 0;

      PVector head = getDot(userId, SimpleOpenNI.SKEL_HEAD);
      if (!(head == null)) {
        all = all + 1;
        fill(255, 0, 0);
        ellipse(head.x, head.y, 10, 10);
        msg.add(head.x);
        msg.add(head.y);
        msg.add(head.z);
      }


      PVector leftShoulder = getDot(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER);
      if (!(leftShoulder == null)) {
        all = all + 1;
        fill(255, 0, 0);
        ellipse(leftShoulder.x, leftShoulder.y, 10, 10);
        msg.add(leftShoulder.x);
        msg.add(leftShoulder.y);
        msg.add(leftShoulder.z);
      }

      PVector rightShoulder = getDot(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER);
      if (!(rightShoulder == null)) {
        all = all + 1;
        fill(255, 0, 0);
        ellipse(rightShoulder.x, rightShoulder.y, 10, 10);
        msg.add(rightShoulder.x);
        msg.add(rightShoulder.y);
        msg.add(rightShoulder.z);
      }

      PVector leftHand = getDot(userId, SimpleOpenNI.SKEL_LEFT_HAND);
      if (!(leftHand == null)) {
        all = all + 1;
        fill(255, 0, 0);
        ellipse(leftHand.x, leftHand.y, 10, 10);
        msg.add(leftHand.x);
        msg.add(leftHand.y);
        msg.add(leftHand.z);
      }

      PVector rightHand = getDot(userId, SimpleOpenNI.SKEL_RIGHT_HAND);
      if (!(rightHand == null)) {
        fill(255, 0, 0);
        ellipse(rightHand.x, rightHand.y, 10, 10);
        msg.add(rightHand.x);
        msg.add(rightHand.y);
        msg.add(rightHand.z);
      }

      PVector leftElbow = getDot(userId, SimpleOpenNI.SKEL_LEFT_ELBOW);
      if (!(leftElbow == null)) {
        all = all + 1;
        fill(255, 0, 0);
        ellipse(leftElbow.x, leftElbow.y, 10, 10);
        msg.add(leftElbow.x);
        msg.add(leftElbow.y);
        msg.add(leftElbow.z);
      }

      PVector rightElbow = getDot(userId, SimpleOpenNI.SKEL_RIGHT_ELBOW);
      if (!(rightElbow == null)) {
        all = all + 1;
        fill(255, 0, 0);
        ellipse(rightElbow.x, rightElbow.y, 10, 10);
        msg.add(rightElbow.x);
        msg.add(rightElbow.y);
        msg.add(rightElbow.z);
      }

      oscP5.send(msg, dest);
    } 
  }
}
//// user-tracking callbacks! for old version on OPENNI
//void onNewUser(int userId) {
//println("start pose detection");
//kinect.startTrackingSkeleton(userId);
//}
//void onEndCalibration(int userId, boolean successful) {
//if (successful) {
//println(" User calibrated !!!");
//kinect.startTrackingSkeleton(userId);
//} else {
//println(" Failed to calibrate user !!!");
//kinect.startPoseDetection("Psi", userId);
//}
//}
//void onStartPose(String pose, int userId) {
//println("Started pose for user");
//kinect.stopPoseDetection(userId);
//kinect.requestCalibrationSkeleton(userId, true);
//}
// -----------------------------------------------------------------
// SimpleOpenNI user events

void onNewUser(SimpleOpenNI curContext, int userId)
{
  println("onNewUser - userId: " + userId);
  println("\tstart tracking skeleton");

  kinect.startTrackingSkeleton(userId);
}

void onLostUser(SimpleOpenNI curContext, int userId)
{
  println("onLostUser - userId: " + userId);
}

void onVisibleUser(SimpleOpenNI curContext, int userId)
{
  //println("onVisibleUser - userId: " + userId);
}


// -----------------------------------------------------------------

