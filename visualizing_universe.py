#Task 2 (optional, extra credits)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation  # we need this to create an animation with matplotlib
from IPython.display import HTML  # we need this to show the animation with a control panel 

fig = plt.figure(figsize=(4,4))
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.plot(0,0,'yo',markersize=16)

r_Earth = 1
r_mars = 2

Earth_orbit = np.linspace(0,2*np.pi, 100)
mars_orbit = np.linspace(0,2*np.pi, 100)

x_Earth = r_Earth*np.cos(Earth_orbit)
y_Earth = r_Earth*np.sin(Earth_orbit)
plt.plot(x_Earth, y_Earth, 'b',lw=1)


x_mars = r_mars*np.cos(mars_orbit)
y_mars = r_mars*np.sin(mars_orbit)
plt.plot(x_mars, y_mars, 'r',linestyle ='dashed', lw=1)


#[DIY1] (optional, extra credits) 
# Q: what is the syntax to plot a "red triangle" at x=3 and  y=5 ? 
# You can write the question and answer as a text cell and include it in your report.
# If you like, you can even add a new code cell, type your answer and show the figure output
# When adding the answer, please specify the DIY number clearly in the text cell or code cell appropriately.

#draw the Earth's orbit as the blue solid line (Background)



# connect x_orbit and y_orbit and generate a blue, solid-line circle "Earth's orbit" (background)
# Set linewidth=1 (or lw=1) 



# ***** create many frames to make an animation --> Earth will be rotating around the Sun following the blue circle *****
# set the number of frames in the animation to be 500 
# If you use Nframe=500, it would take some time (more than minutes) to generate the animation.

Nframes =  50
# Nframes = 500

# initialize
# create an empty class "Earth," to be filled by data points (x,y) along the Earth's orbit for making an animation
# set the marker style to be a blue filled-circle with a size 8


Earth, = plt.plot([],[],'bo',markersize=8)
# mars, = plt.plot([],[],color = 'red', marker = 'D',markersize = 8 )
mars, = plt.plot([],[],'rD',markersize = 8 )



# initiate Earth, and mars, 
def init():
    Earth.set_data([],[])
    mars.set_data([],[])
    return Earth, mars,

# define the function animate(i) by adding stuff to generate frames for Earth, and mars, appropriately
def animate(i):
    x_Earth =  r_Earth*np.cos(-i*rotation)# x= r*cos(theta) where i*rotation = theta_i --> theta_i+1 = theta_i + rotation
    y_Earth =  r_Earth*np.sin(-i*rotation)# y= r*sin(theta)
    Earth.set_data(x_Earth,y_Earth)

    x_mars =  r_mars*np.cos(i*rotation)# x= r*cos(theta) where i*rotation = theta_i --> theta_i+1 = theta_i + rotation
    y_mars =  r_mars*np.sin(i*rotation)# y= r*sin(theta)
    mars.set_data(-x_mars,y_mars)
    return Earth, mars,

# set ranges between [-2, 2] for x- and y-axes
plt.xlim(-2,2)
plt.ylim(-2,2)
# put the title "Mars, Earth, and Sun" fontsize=20
plt.title('Mars, Earth, and Sun',fontsize=20)

# Keep the axes frames
plt.axis('on')
#plt.axis('off')

# set the x- and y- axes scale to be the same
plt.axis('equal')

# makes an animation by repeatedly calling a function func
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = Nframes, interval=10, blit=False)

HTML(anim.to_jshtml())