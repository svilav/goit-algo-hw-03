"""
python koch.py
"""

import turtle


def koch_curve(t, length, order):
    if order == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, length / 3, order - 1)
            t.left(angle)


def koch_snowflake(t, length, order):
    for _ in range(3):
        koch_curve(t, length, order)
        t.right(120)


def main():
    window = turtle.Screen()
    window.title("Koch Snowflake")

    order = int(input("Enter the recursion level (order) of the Koch Snowflake: "))
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    length = 300

    koch_snowflake(t, length, order)

    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    main()
