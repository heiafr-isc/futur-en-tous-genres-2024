#
# Turtle
#

const X0 = 75 # -0..240
const Y0 = 165 # -0..240

const SIZE = 100 # 0..200
const ANGLE = 90 # 0..360

background(0,0,0)
strokeHSV(0, 255, 255)
update()

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

t: Turtle()
t.init()
t.setPos(X0, Y0)

def onDraw():
    t.forward(SIZE)
    t.right(ANGLE)
