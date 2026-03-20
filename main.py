import speed   # 对应总线 1 (SDA.1/SCL.1)
import speeda  # 对应总线 0 (SDA.0/SCL.0)
import time
from enable import drive_control
from stop import brake_control

print("程序启动：正在初始化双总线设备...")

# 1. 分别初始化两个模块
# 总线 1 (引脚 3, 5)
speed.init(address=0x48, bus_id=1, vcc=5.0) 
# 总线 0 (引脚 27, 28)
speeda.init(address=0x48, bus_id=0, vcc=5.0) 

def set_all_voltages(v):
    """同时给两个总线上的设备设置电压"""
    speed.set_voltage(v)  # 发送到总线 1
    speeda.set_voltage(v) # 发送到总线 0

# 配置参数
total_time = 30
steps = 256
interval = total_time / steps

# --- 启动序列 ---
print("解除刹车并开启驱动，准备加速...")
brake_control(0)  # 解除刹车
drive_control(1)  # 开启驱动
time.sleep(0.1)

try:
    for i in range(steps):
        voltage = (i / 255) * 5.0
        
        # 同时控制两个总线的输出
        set_all_voltages(voltage)
        
        if i % 25 == 0:
            print(f"当前同步电压: {voltage:.2f}V | 进度: {i/255*100:.1f}%")
            
        time.sleep(interval)

except KeyboardInterrupt:
    print("\n用户手动停止...")

# --- 停止序列 ---
finally:
    print("\n正在安全关闭设备...")
    set_all_voltages(0) # 两路电压全部归零
    drive_control(0)    # 关闭驱动
    brake_control(1)    # 激活刹车
    print("程序结束：双路已关闭。")
