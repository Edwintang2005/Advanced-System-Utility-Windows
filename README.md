# Advanced-System-Utility-Windows

This tool is designed for windows 10 and provides more in depth information about your system beyond the windows utilities without having an extensive install process. The utility provides quick insights on RAM, CPU, Storage and Battery and quick advice on how to optimise performance. Written purely in Python, this program relies on the Tkinter module and the Psutil module. Flowcharts and diagrams outlining the function of the application are also included.

# Installation
In order to install the program, please copy the .exe file with the .png file into a folder on your computer's local disk. This is because the storage stats provided by the program are of the disk which the program is located. For example, if it was located on a usb, it might only return 1GB free space rather than a 200 GB free space on your computer's hard drive. 

To launch the program, just double click the .exe file as you would any other program and wait for it to start.

Although the program isn't dependent on the .png and will run without it, for the optimal user experience, it is advised that the .png is copied with the program.

The System Monitoring Tool was coded in python with the help of external module Psutil and inbuilt module Tkinter. 

# To Run using source code
In order to run the .py file, you would first need to install psutil.

This is how to install the necessary modules:

1. Check if python is installed by opening cmd and typing python. If it is installed, it will show version
2. If not installed, go to python.org and download the latest version of python. Make sure to tick *add python to path* on the installer
3. Open cmd again and type pip -V to check if pip is functional
4. If pip doesn't work, refer to steps on:
	https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/#:~:text=What%20is%20causing%20the%20%E2%80%98pip%E2%80%99%20is%20not%20recognized,likely%20resolve%20the%20%E2%80%9C%20pip%20is%20not%20

	Otherwise start the next step.
6. To install psutil, open cmd and type pip install psutil
7. The python script should now work when you execute it.
