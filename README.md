# Project_Game 
1. Project name: Secret Room Adventure 

2. Group members: DavidHe0802 Bh0919 WenjunZhen

3. Description: Our project is a command-line game with a 2D-map. The goal of this game is to reach the end point. User is asked for input to choose an option. Options may relate to direction of moving, state of character, or others which can impact the development in this game. The outputs will be the 2D-map which provides useful information to help the user adjust strategy, and each input may update the state of the 2D-map. 

4. Use conda create --name NEWENV --file requirements.txt

import matplotlib.image as mpimg

from matplotlib import pyplot as plt

import numpy as np

import random

You are also expected to upload pictures named blank, character, darkness, floor, hw, vw, pic_flag, pic_goodie, and pic_monster in the same folder where the code is located. All the pictures should be in jpg form and have a size 200*200. 

5. The codebase of our game can be divided into three parts: class definition and initialization, map and item generation, and game interface. The player is expected to run each bulk of code just once, following the order above. After running the game interface, the player is expected to see a map with a character, an endpoint, some monsters, some blocks, and some empty spaces. The player will see the status of the character at the bottom of the map. The play will choose the direction to move by typing in (W/S/A/D). The player will exit the game once E is entered.

![QQ图片20220311162958](https://user-images.githubusercontent.com/100243902/157995679-a44a92aa-958a-41cd-a68e-b202ddc96946.png)

![QQ图片20220311163457](https://user-images.githubusercontent.com/100243902/157995764-6fc36c17-be25-4b6a-b9a5-f0d7727ab2b5.png)

If the player chooses a direction that would result in walking into the wall, the program will kindly remind the player that he/she/they has hit the wall.

![image](https://user-images.githubusercontent.com/100243902/157995792-286f9fdf-fc84-4f8e-b11c-a141bcbe495e.png)

As an exciting adventure game, the player is certainly expected to encounter terrifying monsters. When the player encounters the monster, a series of exciting texts would appear:

![image](https://user-images.githubusercontent.com/100243902/157995813-6c95c567-82b6-407d-ae65-37e49a4ecdce.png)

This text will record your health status as well as the monster’s each time you have attacked each other. At the end, if you successfully killed the monster (by having higher combination of Health and Attack), you will select a goodie as a heritage from the Monster.

![image](https://user-images.githubusercontent.com/100243902/157995827-03dc5eee-2e22-4f74-a702-534e9db40fb1.png)

If you choose Arch or Armor, you will gain corresponding stats. If you choose Torch, nothing will happen, but you will look fancier.

![image](https://user-images.githubusercontent.com/100243902/157995847-92de6b77-d93c-4590-962b-7d1dca00e2a1.png)

Each time you fight a monster or select a goodie, you will see your stats changes correspondingly.

![image](https://user-images.githubusercontent.com/100243902/157995869-f7e3ecc4-a49c-4614-be59-1b7cc5cf1588.png)

After you combat the monsters and eventually arrived the endpoint, you will see the following text appears:

![image](https://user-images.githubusercontent.com/100243902/157995885-88032622-1f08-4bbe-ac60-d0859664b6dd.png)

So say hi to puppycat and feel proud of your amazing journey in our game!

6. If we have more time to develop this program, we can expect this program to have a more diverse map, type of monsters, and goodies for selection. We also expect to improve incorporating animation in the character;s movement among the map, which would require some coding techniques that are more advanced than numpy arrays. 

7. License: MIT license

8. Special thanks to professor Harlin, our TA Shruti, and LA Rachel!



