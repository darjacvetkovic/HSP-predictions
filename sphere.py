import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Times New Roman'
# Define sphere parameters
radius = 13.7 #5

theta = np.linspace(0, 2.*np.pi, 120)
phi = np.linspace(0, np.pi, 120)


x0=17.6 #x0 lingin
y0=12.5 # x0
z0=11 #z0

# Convert to Cartesian coordinates
x = x0 +radius * np.outer(np.cos(theta), np.sin(phi))
y = y0 +radius * np.outer(np.sin(theta), np.sin(phi))
z = z0 +radius * np.outer(np.ones(np.size(theta)), np.cos(phi))

x1 = 14.622192
y1 = 0.128679324
z1 = 0.13240375 

x1_t = 14.76
y1_t = 0
z1_t = 0 

x2 = 18.331923
y2 = 14.652344
z2 = 12.159506

x2_t = 18.5084440188796
y2_t = 14.4
z2_t = 12.2


x3 = 15.668861
y3 = 6.146648
z3 = 15.862966

x3_t = 14.2141263866839
y3_t = 5.7
z3_t = 15.8

# Create a 3D plot
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='3d')
fig.set_tight_layout(True)

# Plot the sphere
ax.plot_surface(x, y, z, color='#0d88e6',alpha=0.2,rstride=12, cstride=5, linewidth=0.3, edgecolor='black')

###
ax.scatter(x0, y0, z0,color='grey')
ax.scatter(x1,y1,z1,color='#b30000',label="predicted value")
ax.scatter(x2,y2,z2,color='#b30000')
ax.scatter(x3,y3,z3,color='#b30000')

# Calculate the point on the sphere's surface (azim and zen in radians)
azim = np.deg2rad(60)  # Change the azimuthal angle as needed
zen = np.deg2rad(90)   # Change the zenith angle as needed

# Calculate the coordinates of the point on the sphere's surface
point_x = x0 + radius * np.sin(zen) * np.cos(azim)
point_y = y0 + radius * np.sin(zen) * np.sin(azim)
point_z = z0 + radius * np.cos(zen)

# Plot the radius line
ax.plot([x0, point_x], [y0, point_y], [z0, point_z], color='#b30000', linestyle='-', linewidth=1, label='R0')

ax.plot([x0, x1], [y0, y1], [z0, z1], color='#8be04e', linestyle='--', label=r'predicted $Ra_{1,2,3}$')
ax.plot([x0, x2], [y0, y2], [z0, z2], color='#8be04e', linestyle='--')
ax.plot([x0, x3], [y0, y3], [z0, z3], color='#8be04e', linestyle='--')
# Add text labels above the lines
text1 = r"$R_{0}$"
ax.text((x0 + point_x) / 2, (y0 + point_y) / 2, (z0 + point_z) / 2, text1, color='#b30000', fontsize=12, verticalalignment='bottom', horizontalalignment='left')

# Add text labels above the lines
text1 = r"$R_{a1}$"
ax.text((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2, text1, color='#474440', fontsize=12, verticalalignment='bottom', horizontalalignment='left')

text2 = r"$R_{a2}$"
ax.text((x0 + x2) / 2, (y0 + y2-4) / 2, (z0 + z2+1) / 2, text2, color='#474440', fontsize=12, verticalalignment='bottom', horizontalalignment='left')

text3 = r"$R_{a3}$"
ax.text((x0 + x3) / 2, (y0 + y3) / 2, (z0 + z3) / 2, text3, color='#474440', fontsize=12, verticalalignment='bottom', horizontalalignment='left')

########### TRUE VALUES ###############
ax.scatter(x1_t,y1_t,z1_t,color='gray',facecolors='none', edgecolors='gray',label="true value")
ax.scatter(x2_t,y2_t,z2_t,color='gray',facecolors='none', edgecolors='gray')
ax.scatter(x3_t,y3_t,z3_t,color='gray',facecolors='none', edgecolors='gray')

ax.plot([x0, x1_t], [y0, y1_t], [z0, z1_t], color='gray', alpha=0.5,linestyle='--', label='true $Ra_{1,2,3}$')
ax.plot([x0, x2_t], [y0, y2], [z0, z2_t], color='gray', alpha=0.5,linestyle='--')
ax.plot([x0, x3_t], [y0, y3_t], [z0, z3_t], color='gray', alpha=0.5,linestyle='--')


text = 'Lignin'#"Human skin permeation rate" 
ax.text(x0-1, y0-1, z0-2, text, color='black', fontsize=11, fontweight='bold', verticalalignment='bottom', horizontalalignment='left')

text = "Cyclohexane"
ax.text(x1, y1, z1, text, color='black', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
text = "Dimethyl sulfoxide"
ax.text(x2, y2-2, z2+2, text, color='black', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
text = "n-Butanol"
ax.text(x3, y3, z3, text, color='black', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
# Add title and labels

#fig.suptitle("HSP sphere")
ax.set_xlabel(r"dispersive forces [$MPa^{1/2}$]",fontsize=14)
ax.set_ylabel(r"polar forces [$MPa^{1/2}$]",fontsize=14)
ax.set_zlabel(r"hydrogen bonding forces[$MPa^{1/2}$]",fontsize=14)


ax.tick_params(axis='x',labelsize=11)
ax.tick_params(axis='y',labelsize=11)
ax.tick_params(axis='z',labelsize=11)

# Adjust aspect ratio
ax.set_box_aspect([1,1,1])#[0.6,1,0.9]


plt.legend(fontsize=11)

#plt.ion()
#fig.savefig("HSPsphere.png",dpi=600)

plt.show()
