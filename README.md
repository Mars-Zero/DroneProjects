# DroneProjects
Some projects with the Ryze Dji Tello drone

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)


## About the Project

This is my collection of projects written mostly in Python with the purpose of completing different tasks with the [Ryze Tello drone](https://www.ryzerobotics.com/tello)

Here is a preview of the scripts in action:
![Preview](/Resources/MarsDroneFacetracking.gif)


There are three different folders: Projects, Modules and Automation.

The Automation folder contains:


* some Python scripts to automate actions for the drone
* repetitive actions of the drone

This part is a work-in-progress

The Modules folder contains:


* an OpenCV script for face detection using Haar Cascades
* a module to register the keyboard as a controller
* a module used to the tweak the image HUE and Saturation(for the Line Follow project) 
* an ImageCapture module to register the stream from the Ryze Tello

The Projects folder contains:


* a script that makes the drone follow the face of a human(FaceTracking.py). Note: The drone must takeoff prior to running the script
* a script to control the drone with the keyboard(KeyboardControl.py). Note: It does not have image streaming from the drone
* a script to control the drone with the keyboard and can take videos and photos(SurveillanceDroneControl.py). 
* a script to map the drone path(controlled with the keyboard) that can be used to return to the takeoff zone(MappingControl.py). Note: Because the drone is very light, it can be moved by the wind, thus the mapping can be inaccurate
* a script that makes drone follow a line that was set prior to the running of the script(also needs to takeoff before the script is running).

## Built With

For the Tello commands, I used this [project](https://github.com/damiafuentes/DJITelloPy) because it already has the commands that are used to control the drone.
As for other packages, I used [NumPy](https://numpy.org) and [OpenCV](https://pypi.org/project/opencv-python/).
The Haar Cascades used in this project are provided [here](https://github.com/opencv/opencv/tree/master/data/haarcascades)




## Run Locally

Clone the project

```bash
  git clone https://github.com/Mars-Zero/DroneProjects
```

Go to the project directory

```bash
  cd DroneProjects
```

Install dependencies

```bash
  python -m pip install pygame
  python -m pip install cv2
  python -m pip install djitellopy
  python -m pip install numpy
```

Start which module you want in the Automation or Projects folders
For example:

```bash
   python -i FaceTracking.py
```

Alternatively, open with your editor of choice and run FaceTracking.py


