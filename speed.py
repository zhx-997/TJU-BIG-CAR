import smbus   #这里是调用的库

# 这里是全局变量   


_bus = None
_address = 0x48
_vcc = 5.0


#每次使用前 你必须初始化一边
def init(address=0x48, bus_id=1, vcc=5.0):
    """
    初始化PCF8591模块（必须在使用其他函数前调用一次）
    :param address: I2C设备地址，默认0x48
    :param bus_id: I2C总线编号，树莓派通常是1
    :param vcc: 供电电压，默认5.0V
    """
    global _bus, _address, _vcc
    _bus = smbus.SMBus(bus_id)
    _address = address
    _vcc = vcc


#实际上你需要调用这个函数 叫做设置电压函数 你需要传入想要的电压
def set_voltage(target_voltage):
    if _bus is None:
        raise RuntimeError("请先调用 init() 初始化模块")
    
    # --- 修改这里：设置不同的上下限 ---
    min_v = 1.0  # 定义最小值
    max_v = 5.0  # 定义最大值

    if target_voltage < min_v:
        target_voltage = min_v
    if target_voltage > max_v:
        target_voltage = max_v
    # --------------------------------

    # 将电压转换为8位数字 (0-255)
    digital_value = int(target_voltage / _vcc * 255)

    _bus.write_byte_data(_address, 0x40, digital_value)
    print(f"[speed-Bus1] 输出电压: {target_voltage:.2f}V (范围: {min_v}-{max_v}V)")

def init_conversion():
    """
    有些模块需要先进行一次空读来启动转换
    """
    if _bus is None:
        raise RuntimeError("请先调用 init() 初始化模块")
    _bus.read_byte(_address)
