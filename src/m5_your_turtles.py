"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Peter Venema.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
Sen = rg.SimpleTurtle()
Roy =  rg.SimpleTurtle()
Sen.pen = rg.Pen('blue', 2)
Roy.pen = rg.Pen('orange',2)
Sen.speed = 10
Roy.speed = 10
Roy.pen_up()
Roy.right(90)
Roy.forward(200)
Roy.left(90)
for k in range (20):
    size = 100 - (k*5)
    Sen.draw_circle(size)
    Sen.pen_up()
    Sen.left(90)
    Sen.forward(10-2*k)
    Sen.right(90)
    Sen.pen_down()
    Roy.pen_down()
    Roy.draw_circle(size)
    Roy.pen_up()
    Roy.left(90)
    Roy.forward(-10+2*k)
    Roy.right(90)
    Roy.pen_down()
Biv = rg.SimpleTurtle()
Biv.speed = 10
Biv.pen_up()
Biv.left(90)
Biv.forward(200)
Biv.pen_down()
Biv.right(270)
Biv.draw_circle(215)
window.close_on_mouse_click()