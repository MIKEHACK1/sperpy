import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Genera i dati per la sfera
radius = 1
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
x = radius * np.outer(np.cos(theta), np.sin(phi))
y = radius * np.outer(np.sin(theta), np.sin(phi))
z = radius * np.outer(np.ones(np.size(theta)), np.cos(phi))

# Crea la figura e l'asse 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Disegna la sfera
ax.plot_surface(x, y, z, color='b', alpha=0.6, edgecolor='k')

# Imposta gli assi x, y, z
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Imposta il titolo del grafico
plt.title('Sfera')

# Mostra il grafico
plt.show()
