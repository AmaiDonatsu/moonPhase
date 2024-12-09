import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')

plt.close('all')

##########3



# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear una figura con dos subplots en una fila (1 fila, 2 columnas)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))  # 1 fila, 2 columnas

# Primer plot
ax[0].plot(x, y1, label='sin(x)', color='blue')
ax[0].set_title('Seno')
ax[0].legend()

# Segundo plot
ax[1].plot(x, y2, label='cos(x)', color='red')
ax[1].set_title('Coseno')
ax[1].legend()

# Ajustar diseño para evitar superposición
plt.tight_layout()

# Mostrar los plots
plt.show()
