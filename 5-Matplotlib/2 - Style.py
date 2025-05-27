import matplotlib.pyplot as plt
import numpy as np

#   Colours

    #   'b' - Blue
    #   'g' - Green
    #   'r' - Red
    #   'c' - Cyan
    #   'm' - Magenta
    #   'y' - Yellow
    #   'k' - Black
    #   'w' - White

#   Markers
    #   '.' - Point Marker
    #   'o' - Circle Marker
    #   'x' - X Marker
    #   'D' - Diamond Marker
    #   'H' - Hexagon Marker
    #   's' - Square Marker
    #   '+' - Plus Marker
    #   '^' - Triangle Marker

#   Styles
    #   '-' - Solid Line
    #   '_' - Dashed Line
    #   '-.' - Dash-Dot Line
    #   ':' - Dotted Line


#   plt.plot(X-axis, Y-axis, 'color>marker>style)


x = [1,2,3,4,5,6,7,8,9]
plt.plot(x, np.power(x,2), 'g+:', x, np.power(x,3), 'ro-')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Styles Plot')

plt.show()