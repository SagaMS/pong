import turtle

window = turtle.Screen()
window.title('Ping Pong')
window.bgcolor('salmon')
window.setup(width=800, height=600)
window.tracer()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("blue")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color("green")
ball.goto(0, 0)
ball.penup()

#loop
while True:
    window.update()
