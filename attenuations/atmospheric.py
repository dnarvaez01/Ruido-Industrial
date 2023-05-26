from typing import Optional
import pandas as pd

atm_coefficients = pd.read_csv("attenuations\coeficientes temperatura.txt", delimiter=" ")
humidity_values = atm_coefficients['%'].values
temperature_values = atm_coefficients['°C'].values

def alpha_atm(temperature: Optional[int]=10, humidity:Optional[int]=70):
    if humidity not in humidity_values:
        return f'el valor {humidity} no se encuentra en la tabla'
    if temperature not in temperature_values:
        return f'el valor {temperature} no se encuentra en la tabla'
    return atm_coefficients.loc[(atm_coefficients['%']==humidity) &
                                (atm_coefficients['°C']==temperature)].drop(columns=['%', '°C']).values

def atm_attenuation(distance:float, temperature: Optional[int]=10, humidity:Optional[int]=70):
    alpha = alpha_atm(temperature, humidity)[0]
    return distance*alpha/1000
