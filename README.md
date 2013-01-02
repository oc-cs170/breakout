breakout
========

A basic breakout game using PyGame.

The program consists of three modules:

* breakout.py       - Contains the game loop and runs the game
* Ball.py           - A class to create, update, and draw the ball
* Paddle.py         - A class to create, update, and draw the paddle

To-do
-----

1. Constrain the paddle so that no pixels leave the screen by limiting movement
2. Constrain the ball so that no pixels leave the screen by adding reflection
3. Implement a "round" that ends when a ball touches the bottom of the screen
4. Implement a "game" that ends when 3 rounds have ended
5. Build a "wall" of "bricks" that includes 5 courses of 10 bricks
6. Detect ball/brick collisions, remove brick(s), reflect ball
