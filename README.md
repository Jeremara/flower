`Flower Drawing with Username`
`Description`
This Python script uses the turtle module to draw a colorful flower pattern and display a username input by the user. The script creates a GUI window with a title "Flower Drawing with Username" and prompts the user to enter their name. After entering the username, the script draws a flower pattern with gradually changing colors and displays the username at the bottom of the window.

`Functions`
draw_flowers()
  Sets the turtle speed to 0 (fastest) and background color to black.
  Loops 16 times to draw 16 flowers with different colors.
  Each flower is drawn using two circles with a 90-degree right turn in between.
  The color of each flower is generated using the colorsys.hsv_to_rgb function, which converts HSV (Hue, Saturation, Value) colors to RGB (Red, Green, Blue) colors.
  The hue value is incremented by 0.005 for each flower to create a gradual color change.
  print_username(username)
  Moves the turtle to the bottom of the window (0, -250) and writes the username in white color with a font size of 24.

main()
  Creates a turtle screen with a title "Flower Drawing with Username".
  Prompts the user to enter their name using a text input dialog box.
  Calls the draw_flowers() and print_username(username) functions to draw the flowers and display the username.
  Waits for the user to close the window using the done() function.
  
`Usage`
  Save this script as a Python file (e.g., flower_drawing.py).
  Run the script using Python (e.g., python flower_drawing.py).
  Enter your name when prompted by the input dialog box.
  Enjoy the colorful flower pattern with your username displayed at the bottom!
  
`Requirements`
  Python 3.x
  Turtle module (comes with Python standard library)
  
`License`
This script is released under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.
