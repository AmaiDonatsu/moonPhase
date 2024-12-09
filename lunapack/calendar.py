import matplotlib.pyplot as plt
import math

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
        grid_dims = math.floor(filtred_len)
        plt.figure(figsize=(10,10))

        for i in range(filtred_len):
            plt.subplot 


        return calendar_format

