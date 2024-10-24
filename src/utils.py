from telebot.types import Message


def scale(num: str, data: str) -> str:
    numx = 0
    if not num.isdigit():
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
    if int(nums[0]) == 10:
        ans = 10**float(nums[1])
    else:
        ans = float(nums[0])*10**float(nums[1])
    if ans.is_integer():
        return int(ans)
    return ans

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
