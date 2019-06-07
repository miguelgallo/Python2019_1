import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import matplotlib.animation as animation
import subprocess

def simple_pendulum_deriv(x, t, m, g, l): 
    """The simple pendulum subject to zero damping and zero control input
    Based on material from the MIT OCW subject "Underactuated Robotics"
    "lecture 2: the simple pendulum" given by Russell Tedrake, the 
    maths and some of the related diagrams are given at about 51 minutes
    in.
    """
    nx = np.zeros(2)
    nx[0] = x[1]
    nx[1] = -(m * g * l * np.sin(x[0])) 
    return nx

x0 = [np.pi - 0.1, 0.0]
t = np.linspace(0.0, 50.0, 1001)
sol = odeint(simple_pendulum_deriv, x0, t, args = (0.2, 9.8, 1.0))

fig = plt.figure(figsize=(5, 5), facecolor='w')
ax = fig.add_subplot(1, 1, 1)
plt.rcParams['font.size'] = 15

lns = []
for i in range(len(sol)):
    ln, = ax.plot([0, np.sin(sol[i, 0])], [0, -np.cos(sol[i, 0])],
                  color='k', lw=2)
    tm = ax.text(-1, 0.9, 'time = %.1fs' % t[i])
    lns.append([ln, tm])
ax.set_aspect('equal', 'datalim')
ax.grid()
ani = animation.ArtistAnimation(fig, lns, interval=50)

fn = 'odeint_single_pendulum_artistanimation'
ani.save(fn+'.mp4',writer='ffmpeg',fps=1000/50)
ani.save(fn+'.gif',writer='imagemagick',fps=1000/50)

cmd = 'magick convert %s.gif -fuzz 10%% -layers Optimize %s_r.gif'%(fn,fn)
subprocess.check_output(cmd)

plt.rcParams['animation.html'] = 'html5'
ani
