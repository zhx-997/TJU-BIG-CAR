from gpiozero import LED

# 初始化 BCM 21 引脚
# 默认设为不刹车状态 (输出 3.3V)
_brake_pin = LED(21, initial_value=True)

def brake_control(state):
    """
    控制刹车状态
    :param state: 1 表示刹车 (输出 0V)，0 表示不刹车 (输出 3.3V)
    """
    if state == 1:
        _brake_pin.off()  # 输出 0V (低电平)
    else:
        _brake_pin.on()   # 输出 3.3V (高电平)
    
    action = "【刹车激活】" if state == 1 else "【解除刹车】"
    print(f"执行：{action}，GPIO21 输出 {'0V' if state == 1 else '3.3V'}")
