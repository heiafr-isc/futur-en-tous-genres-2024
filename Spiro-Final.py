################################################################################
# @brief       : Simulateur de Spirographe
# @author      : Jacques Supcik <jacques.supcik@hefr.ch>
# @date        : 5. Novembre 2024
# ------------------------------------------------------------------------------
# @copyright   : Copyright (c) 2024 HEIA-FR / ISC
#                Haute école d'ingénierie et d'architecture de Fribourg
#                Informatique et Systèmes de Communication
# @attention   : SPDX-License-Identifier: MIT OR Apache-2.0
################################################################################

const GRAND_RAYON = 120 #  0..120
const PETIT_RAYON = 66 # 0..120
const RAYON_STYLO = 48 # 0..120
const VITESSE = 11 # 1..30
const COULEUR = 58 # HUE
const INCREMENT_COULEUR = 67 # 0..200

petit_rayon = PETIT_RAYON
rayon_stylo = RAYON_STYLO

class Spinograph:
    alpha: float
    pos: vector
    
    # Calcule la position du stylo (pos) en fonction de l'angle alpha
    def setPos():
        center: vector
        beta: float
        # Calcule la position du centre du petit cercle
        center.x = 120.0 + toFloat((GRAND_RAYON - PETIT_RAYON)) * sin(rad(alpha))
        center.y = 120.0 + toFloat(GRAND_RAYON - PETIT_RAYON) * cos(rad(alpha)) 
        # Calcule l'angle de rtation du petit cercle
        beta = alpha * toFloat(GRAND_RAYON) / toFloat(PETIT_RAYON)
        # Calcule la position du style
        pos.x = center.x - toFloat(RAYON_STYLO) * sin(rad(alpha - beta))
        pos.y = center.y - toFloat(RAYON_STYLO) * cos(rad(alpha - beta))

    # Initialise le Spirographe
    def init()
        alpha = 0
        setPos()
        # Dessine un cercle blanc (grand cercle)
        stroke(100,100,100)
        drawCircle(120, 120, GRAND_RAYON)
        textFont(FONT_ROBOTO_16)
        drawTextCentered(20,222, petit_rayon)
        drawTextCentered(220,222, rayon_stylo)

        update()

    # Dessine le segment de la position actuelle vers la nouvelle position après
    # avoiur ajouté `delta_a` à l'angle alpha.
    def draw(delta_a):
        # Récupère la position actuelle
        x0 = round(pos.x)
        y0 = round(pos.y)
        # Ajoute `delta_a` à l'angle alpha.
        alpha = alpha + toFloat(delta_a)
        # Calcule la nouvelle position
        setPos()
        # Récupère la nouvelle position
        x1 = round(pos.x)
        y1 = round(pos.y)
        # Tire un trait de l'ancienne position vers la nouvelle
        drawLine(x0, y0, x1, y1)
        update()

background(0,0,0)
s: Spinograph
s.init()
c = toFloat(COULEUR)
update()

def onDraw():
    strokeHSV(c, 255, 255)
    s.draw(VITESSE)
    # Calcule la nouvelle couleur
    c = (c + (toFloat(INCREMENT_COULEUR) * toFloat(VITESSE))/100.0)
    # Corrige la valeur de la couleur si celle-ci est plus grande ou égale que 256
    while (c >= 256):
        c = c - 256

def onClick():
    b:buttons = getButtons()
    if b.left:
        if petit_rayon - 5 >= 0:
            background(0,0,0)
            petit_rayon = petit_rayon - 5
            s.init()
    if b.right:
        background(0,0,0)
        petit_rayon = petit_rayon + 5
        s.init()
    if b.up:
        background(0,0,0)
        rayon_stylo = rayon_stylo + 5
        s.init()
    if b.down:
        if rayon_stylo - 5 >= 0:
            background(0,0,0)
            rayon_stylo = rayon_stylo - 5
            s.init()
    if b.middle:
            background(0,0,0)
            s.init()

    