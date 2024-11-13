#
# Tortue
#

const X0 = 75 # -0..240
const Y0 = 165 # -0..240

const TAILLE = 100 # 0..200
const ANGLE = 90 # 0..360

background(0,0,0)
strokeHSV(0, 255, 255)
update()

class Tortue:
    position: vector
    dir: vector
    crayon_pose: bool

    def maison():
        position = vector(x=120,y=120)

    def init():
        crayon_pose = true
        dir.fromAngle(rad(-90))
        maison()

    def enAvant(steps):
        dir.mulScalar(steps)
        target = position
        target.add(dir)
        x0 = round(position.x)
        y0 = round(position.y)
        x1 = round(target.x)
        y1 = round(target.y)
        if crayon_pose:
            drawLine(x0, y0, x1, y1)
            update()
        position = target

    def aDroite(deg):
        dir.fromAngle(dir.angle() + rad(deg))

    def aGauche(deg):
        aDroite(-deg)

    def leveLeCrayon():
        crayon_pose = false

    def poseLeCrayon():
        crayon_pose = true

    def DefinitPosition(x1,y1):
        position = vector(x=x1,y=y1)

t: Tortue()
t.init()
t.DefinitPosition(X0, Y0)

def onDraw():
    t.enAvant(TAILLE)
    t.aDroite(ANGLE)
