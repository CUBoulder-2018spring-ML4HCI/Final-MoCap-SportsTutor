# Final-MoCap-SportsTutor
A machine-learning based virtual sports coach.
Designed and built by  
* Jonathan Fermin
* Jonathan Meade
* Stacia Near
* Christoph Uhl
* Michael Vienneau  

For CSCI-4830 with Prof. Ben Shapiro and Asst. Prof. William Temple  
## Summary
Using data collected during in-person coaching sessions with a profesisonal sports coach, our system is able to analyze the movements of a user
without their coach present and provide feedback and tips on improving form and motion. View our full project proposal at `docs/proposal.pdf`.

## Setup
### Hardware
For this project, you will need one Unix-based or Macintosh system and one Windows system (preferably Windows 8 or above).

##### 3 Microbits
* 2 Batteries each
* Load `microbit/microbit-receiver.hex` onto one microbit
* Load `microbit/microbit-transmit1.hex` onto another microbit
* Load `microbit/microbit-transmit2.hex` onto the last microbit

##### Kinect
* Place black backdrop behind you for a better read.
* Connect Kinect to Windows computer.
* Ensure you have installed the Kinect packages listed below in software dependencies.
* Edit the skeleton.config folder found in `SkeletonBasics-D2D/Debug/skeleton.config` to hold the IP address of your Macintosh system.

### Software
#### Dependencies include:
##### GUI
Make sure pip is on your computer even if you are using Windows, you can run it from the cmd app if you choose "run as administrator."

* pip install PyQt5
* pip install SIP
* pip install numpy
* pip install dtw
* pip install sklearn

##### Kinect
* Need a Windows OS to run
[Kinect Developer's Toolkit](https://www.microsoft.com/en-gb/download/details.aspx?id=40276)
[Kinect SDK](https://www.microsoft.com/en-gb/download/details.aspx?id=40278)

##### Execute the Following:
* `python-gui/SportsTutor/main.py`
* `SerialPortReading/SerialPortReading.pde`
* `processingMerge/processingMerge.pde`
