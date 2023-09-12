# MachineLearningGame-ZombieKiller 🧟

[![Python](https://img.shields.io/badge/python-3.11.4-blue)]
[![Pygame Library](https://img.shields.io/badge/pygame-2.4.0-green)]
[![OpenCV CV2 Library](https://img.shields.io/badge/opencv_python%20(cv2)-4.8-pink)]
[![Mediapine](https://img.shields.io/badge/mediapipe-0.10.3-orange)]
[![Numpy](https://img.shields.io/badge/numpy-1.25.2-yellow)]
[![License](https://img.shields.io/badge/license-MIT_License-purple)]
[![Message](https://img.shields.io/badge/Clone_project_and_enjoy_the_game_%F0%9F%98%89-8A2BE2)]
## The innovation
The idea came up with the mosquito terminator game on pysource.com 😉
## Introduction 
This is the Computer Vision Game developed by myself. </br>
The game consists of zombies and angels flying in the center of the screen. Every time you swat a zombie you get 1 point and every time you swat an angel you lose 1 point. In case you swat multiple zombies, you will get multiple points; the same applies to swatting angels. Everything must be done within a certain number of seconds. This is the image of the Game.'
</br>
![image](https://github.com/tovanhieu/MachineLearningGame-ZombieKiller/assets/26000753/0b58801e-6ea4-4031-af73-991212b95d48)
</br>
The game integrated tracking of the movements of the body with OpenCV. For the tracking of the hand gesture, which will be the joypad of our game, I used MediaPipe.
MediaPipe is a library deveploped by google ready to use and for multiple functions, for my project, just a few commands are enough and we manage to have 21 points of the hand. If you want more details on hand tracking I suggest you read the official [MediaPipe Hands guide](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) 
</br>
<img width="950" alt="hand-landmarks" src="https://github.com/tovanhieu/MachineLearningGame-ZombieKiller/assets/26000753/3b511d80-141e-4331-b9bf-682ae466a362">
<br>
<img decoding="async" width="300" height="564" src="https://pysource.com/wp-content/uploads/2021/08/hand_tracking_3d_android_gpu.gif" alt="Computer Vision Game MediaPipe hand" title="Computer Vision Game MediaPipe hand">


## How to run the game
Clone the project and install all the needed packages, to run the game following command line:
<br>
    ```
    $ python main.py
    ```
## Future work
Depend on your purpose and idea, the game can be developed some features in the future, there are some of my recommendations 💁‍♂️:
1. **Two players at one time**
2. **Create more levels with correspond screen**
3. **Set a target score for each level if the player could not reach the score the game have to reset to the first level**
4. ...etc...
## Summury
Hope you have a wonderfull time with my project, enjoy it and don't forget to follow and drop me a star🌟 on my repo in github 😊
