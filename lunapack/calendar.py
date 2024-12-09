import matplotlib.pyplot as plt
import matplotlib
import math
import numpy as np

matplotlib.use('Qt5Agg')


def generate_calendar(calendar_format, *args, **kwargs):
    if len(calendar_format) > 0:
        filtred = []

        if kwargs:
            for calendar_vignette in calendar_format:
                for key, value in kwargs.items():
                    if key in calendar_vignette and value == calendar_vignette[key]:
                        filtred.append(calendar_format)
        else:
            filtred = calendar_format

        filtred_len = len(filtred)
        grid_dims = math.floor(np.sqrt(filtred_len))
        print(filtred_len)
        print(grid_dims)

        if filtred_len > 0:

            plt.close('all')
            fig, ax = plt.subplots(grid_dims + 1, grid_dims, figsize=(10, 8))  
            ax = ax.ravel()  

            x = np.linspace(0, 10, 100)
            y1 = np.sin(x)

            
            for i in range(min(filtred_len, len(ax))):  
                try:
                    ax[i].plot(x, y1, label='sin(x)', color='blue')
                    ax[i].set_title(f'Seno {i+1}')
                    ax[i].legend()
                except Exception as e:
                    print(f"Uy, falló en el índice {i}: {e}")

            
            for j in range(filtred_len, len(ax)):
                fig.delaxes(ax[j])  

            plt.tight_layout()
            plt.show()
        

        return calendar_format





