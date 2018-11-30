
# coding: utf-8

# In[1]:

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def years_to_wait(your_age, partners_age):
    global years
    years = 0
    while (your_age/2+7) > partners_age:
        years += 1
        your_age += 1
        partners_age += 1

you = list(range(15, 100))
partner = list(range(15, 100))
datalist = []
data = np.array(datalist)
for m in you:
    for f in partner:
        years_to_wait(your_age = m, partners_age = f)
        datalist.append(years)
y_values = np.array(datalist)
y_values1 = np.hsplit(y_values, 85)

#draw plot

fig, ax = plt.subplots()
im = ax.imshow(y_values1, cmap = 'RdYlGn_r') 
plt.xlim (xmax = 42, xmin = 0)
plt.ylim (ymax = 15, ymin = 80)
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")

ax.set_title("How long you have to wait for your love to become socially accepted").set_position([.5, 1.02])
ax.set_xlabel('Your Partner\'s Age')
ax.set_ylabel('Your Age')

cbar = plt.colorbar(im) 
cbar.set_label('Years to wait until socially accepted')

fig.tight_layout()
#plt.savefig('Years until accepted_1.png', format='png', dpi=700)
plt.show()


# In[ ]:



