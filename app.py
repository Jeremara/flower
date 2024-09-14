from turtle import *
import colorsys
import turtle

# Function to draw flowers
def draw_flowers():
    speed(0)
    bgcolor('black')
    p = 0
    for i in range(16):
        for j in range(18):
            q = colorsys.hsv_to_rgb(p, 1, 1)
            color(q)
            p += 0.005
            rt(90)
            circle(150 - j * 6, 90)
            lt(90)
            circle(150 - j * 6, 90)
            rt(180)
        circle(40, 24)

# Function to print username
def print_username(username):
    penup()
    goto(0, -250)  
    pendown()
    color('white')
    write(username, align="center", font=("Arial", 24, "normal"))

# Main function
def main():
    screen = turtle.Screen()
    screen.title("Flower Drawing with Username")
    
    # Create an input dialog box
    username = screen.textinput("Input", "Enter your name:")
    
    draw_flowers()
    print_username(username)
    done()

if __name__ == "__main__":
    main()