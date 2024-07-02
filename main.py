import turtle
t = turtle.Turtle()

def draw_branch(branch_length, angle, scale_factor, min_length):
    if branch_length > min_length:
        t.forward(branch_length)
        t.right(angle)
        draw_branch(branch_length * scale_factor, angle, scale_factor, min_length)
        t.left(2 * angle)
        draw_branch(branch_length * scale_factor, angle, scale_factor, min_length)
        t.right(angle)
        t.backward(branch_length)

# Set up the screen and turtle
t.speed('fastest')
t.left(90)
t.up()
t.backward(100)
t.down()
t.color('green')

# Parameters: branch length, angle, scale factor, minimum branch length
draw_branch(100, 30, 0.7, 5)

# Finish drawing
t.done()
