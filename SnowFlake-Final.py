#
# Snow Flake Final Version
#

const FLAKE_SIZE = 200 # 0..200
const FLAKE_DEPTH = 2 # 0..4
const FLAKE_COLOR = 40 # HUE

background(0,0,0)
strokeHSV(FLAKE_COLOR, 255, 255)
update()

depth = FLAKE_DEPTH
drawing = true

class Turtle:
    pos: vector
    dir: vector
    pen_down: bool

    def home():
        pos = vector(x=120,y=120)

    def init():
        pen_down = true
        dir.fromAngle(rad(-90))
        home()

    def forward(steps):
        dir.mulScalar(steps)
        target = pos
        target.add(dir)
        x0 = round(pos.x)
        y0 = round(pos.y)
        x1 = round(target.x)
        y1 = round(target.y)
        if pen_down:
            drawLine(x0, y0, x1, y1)
            update()
        pos = target

    def right(deg):
        dir.fromAngle(dir.angle() + rad(deg))

    def left(deg):
        right(-deg)

    def penUp():
        pen_down = false

    def penDown():
        pen_down = true

    def setPos(x1,y1):
        pos = vector(x=x1,y=y1)

class SnowFlake:
    turtle: Turtle

    def init()
        turtle.init()
        x0 = 120.0 - (toFloat(FLAKE_SIZE) /  2)
        y0 = 120.0 + toFloat(FLAKE_SIZE) * tan(rad(30)) / 2
        turtle.setPos(x0, y0)
        turtle.right(90)

    def line(l, n):
        if n > 0:
            line(l/3, n-1)
            turtle.right(60)
            line(l/3, n-1)
            turtle.left(120)
            line(l/3, n-1)
            turtle.right(60)
            line(l/3, n-1)
        else:
            turtle.forward(l)

    def draw(size, depth):
        for i in 3:
            line(size, depth)
            turtle.left(120)
        

def onClick():
    b:buttons = getButtons()
    if b.left:
        if depth > 0:
            depth = depth - 1
            background(0,0,0)
            drawing = true
    if b.right:
        if depth < 4:
            depth = depth + 1
            background(0,0,0)
            drawing = true

def onDraw():
    if drawing:
	    snowFlake: SnowFlake    
        snowFlake.init()
        snowFlake.draw(FLAKE_SIZE, depth)
        drawing = false
