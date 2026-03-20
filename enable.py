from gpiozero import LED

# 初始化 GPIO 17
# initial_value=False 意味着一开始输出 0V
_pin = LED(17, initial_value=False)

def drive_control(state):
    """
    state=1: 开车 (0V) -> pin.off()
    state=0: 停车 (3.3V) -> pin.on()
    """
    if state == 1:
        _pin.off()  # 输出 0V
    else:
        _pin.on()   # 输出 3.3V
    
    status = "开车 (0V)" if state == 1 else "停车 (3.3V)"
    print(f"GPIO 状态切换为: {status}")
