# Installing components for GUI

Make sure pip is on your computer even if you are using Windows, you can run it from the cmd app if you choose "run as administrator."

#If you just want to run the code:

## Get SIP

Installation instructions: https://www.riverbankcomputing.com/software/sip/download

Type:
pip3 install SIP

## Get PyQt5

Instructions: https://www.riverbankcomputing.com/software/pyqt/download5

It has to be version 5, because it is not backwards compatible.

Type:
pip3 install PyQt5

#If you need to edit the UI layout, move buttons around, etc:

## Get Qt Designer (NOT Creator)

https://stackoverflow.com/a/42091035/8711488

pip install pyqt5-tools
Find in ...\Python36\Lib\site-packages\pyqt5-tools\designer\designer.exe


## Get Qt (Optional?)

Download site: https://www.qt.io/

This has some additional resources in it, but I think PyQt actually already has all the functionality to be able to run the UI components. To get it, go to the downloads section and make sure to download the Open Source version, not the Free Trial of Commercial version!
