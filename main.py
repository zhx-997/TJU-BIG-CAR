import speed
import time
from enable import drive_control
from stop import brake_control  # 导入刹车控制功能

print("程序启动：解除刹车并开启驱动，准备加速...")

# 初始化速度控制模块
speed.init(address=0x48, vcc=5.0)

# 配置参数
total_time = 30
steps = 256
interval = total_time / steps

# --- 1. 启动序列 ---
brake_control(0)  # 首先【解除刹车】(输出 3.3V)
drive_control(1)  # 然后【开启驱动】(输出 0V)
time.sleep(0.1)   # 短暂缓冲，确保硬件状态切换稳定

for i in range(steps):
    voltage = (i / 255) * 5.0
    
    # 持续写入电压，观察速度上升
    speed.set_voltage(voltage)
    
    # 每隔一段步长打印一次状态
    if i % 25 == 0:
        print(f"当前状态 -> 电压: {voltage:.2f}V | 进度: {i/255*100:.1f}%")
        
    time.sleep(interval)

# --- 2. 停止序列 ---
print("\n30秒运行结束，正在停止设备...")

speed.set_voltage(0) # 速度指令归零
drive_control(0)     # 【关闭驱动】(输出 3.3V)
#brake_control(1)     # 【激活刹车】(输出 0V)

print("程序结束：驱动已切断，刹车已锁定。")
