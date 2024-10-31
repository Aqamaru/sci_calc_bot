from math import pi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.signal import find_peaks, peak_widths

matplotlib.use('agg')

def calculate_s() -> None:
    z = []
    with open('specter.txt', 'r') as file :
        z = file.readlines()
    y = []  
    for i in z:
        y.append(int(i))

    x = np.array(y)
    peaks, _ = find_peaks(x)
    half = peak_widths(x, peaks, rel_height=0.5)

    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.hlines(*half[1:], color = "C2")
    plt.savefig("graph.png")
    return

def calculate_f(data: str, avg_power: str, freq: str, diameter: str) -> str:
    nump = 0
    numf = 0
    numd = 0
    if ('*10^' in avg_power):
        nump = from_si(avg_power)
    else:
        nump = float(avg_power)
    if ('*10^' in freq):
        numf = from_si(freq)
    else:
        numf = float(freq)
    if ('*10^' in diameter):
        numd = from_si(diameter)
    else:
        numd = float(diameter)
    
    square = pi * (numd**2/4)

    if ('gausian' in data):
        return f"{nump/(numf*square/2)} Дж/см^2"
    return f"{nump/(numf*square)} Дж/см^2"

def convert(quantity_value: str, data: str, velocity: str = "" ) -> str:
    PLANKO = 6.62*10**(-34)
    numq = 0
    if ('*10^' in quantity_value):
        numq = from_si(quantity_value)
    else:
        numq = float(quantity_value)

    numv = 0
    if not velocity == "":
        if not velocity.isdigit():
            numv = from_si(velocity)
        else:
            numv = float(velocity)
    data = data.replace('convert_from_', '').replace('to_', '')
    data_l = data.split('_')
    match data_l[1]:
        case "waveifrequency":
            match data_l[0]:
                case "waveifrequency":
                    return f"{to_si(numq)} {quantities['waveifrequency']}"
                case "waveilenght":
                    return f"{to_si(numv/numq)} {quantities['waveifrequency']}"
                case "photonienergy":
                    return f"{to_si(numq/PLANKO)} {quantities['waveifrequency']}"
        case "waveilenght":
            match data_l[0]:
                case "waveifrequency":
                    return f"{to_si(numv/numq)} {quantities['waveilenght']}"
                case "waveilenght":
                    return f"{to_si(numq)} {quantities['waveilenght']}"
                case "photonienergy":
                    return f"{to_si((PLANKO*numv)/numq)} {quantities['waveilenght']}"
        case "photonienergy":
            match data_l[0]:
                case "waveifrequency":
                    return f"{to_si(PLANKO*numq)} {quantities['photonienergy']}"
                case "waveilenght":
                    return f"{to_si((PLANKO*numv)/numq)} {quantities['photonienergy']}"
                case "photonienergy":
                    return f"{to_si(numq)} {quantities['photonienergy']}"
    return ""

def scale(num: str, data: str) -> str:
    numx = 0
    if num.count('*10^') != 0:
        numx = from_si(num)
    else:
        numx = float(num)
    data = data.replace('scale_from_', '').replace('to_', '')
    scales = data.split('_')
    numx = numx*10**scale_pows[scales[0]]
    numx = numx/10**scale_pows[scales[1]]
    return to_si(numx)

def to_si(num: int | float) -> str:
    power: int = 0
    if num > 9 and num != 10:
        while num > 9:
            num = num/10
            power+=1
            if num.is_integer():
                num = int(num)
        if power < 4:
            return f"{num*10**power}"
        if num == 1:
            return f"10^{power}"
        return f"{num}*10^{power}"
    if num < 0.1:
        while num < 0.1:
            num = num*10
            power-=1
            if num.is_integer():
                num = int(num)
        if power > -4:
            return f"{num*10**power}"
        if num == 1:
            return f"10^{power}"
        return f"{num}*10^{power}"
    if num.is_integer():
        return f"{int(num)}"
    return f"{num}"

def from_si(num: str) -> int | float:
    num = num.replace('*10', '')
    nums = num.split('^')
    if float(nums[0]) == 10:
        ans = 10**float(nums[1])
    else:
        ans = float(nums[0])*10**float(nums[1])
    if ans.is_integer():
        return int(ans)
    return ans

quantities = {
        'waveifrequency' : 'Гц',
        'waveilenght' : 'м',
        'photonienergy': 'Дж'
        }

scale_pows = {
        'quecto': -30,
        'ronto': -27,
        'yocto': -24,
        'zepto': -21,
        'atto': -18,
        'femto': -15,
        'pico': -12,
        'nano': -9,
        'micro': -6,
        'mili': -3,
        'centi': -2,
        'deci': -1,
        'none': 0,
        'deca': 1,
        'hecto': 2,
        'kilo': 3,
        'mega': 6,
        'giga': 9,
        'tera': 12,
        'peta': 15,
        'exa': 18,
        'zetta': 21,
        'yotta': 24,
        'ronna': 27,
        'quetta': 30
        }
