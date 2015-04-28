import pygal
from math import cos

chart1 = pygal.XY(show_dots = False, show_y_labels = False)

chart1.title = 'Amplitude Modulation'
chart1.add('Carrier Signal', [(x, cos(20*x)) for x in range(0,200,1)])
chart1.add('Message Signal', [(x, cos(.1*x)+5) for x in range(0,200,1)])
chart1.add('AM Signal', [(x, ((1 + cos(.1*x)) * cos(20*x))+10) for x in range(0,200,1)])
chart1.render_to_file('combined.svg')

