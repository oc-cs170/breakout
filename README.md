breakout
========

A basic breakout game using PyGame.

The program consists of three modules:

* breakout.py       - Contains the game loop and runs the game
* ball.py           - A class to create, update, and draw the ball
* paddle.py         - A class to create, update, and draw the paddle

To-do
-----

1. Constrain the paddle so that no pixels leave the screen by limiting movement (Done)
2. Constrain the ball so that no pixels leave the screen by adding reflection
3. Detect ball/paddle collisions, reflect ball
4. Implement a "round" that ends when a ball touches the bottom of the screen
5. Implement a "game" that ends when 3 rounds have ended
6. Build a "wall" of "bricks" that includes 5 courses of 10 bricks
7. Detect ball/brick collisions, remove brick(s), reflect ball
