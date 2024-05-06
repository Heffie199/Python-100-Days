import serial
import time
# 打开串口
ser = serial.Serial('COM5', 115200)  # 请根据实际串口和波特率进行修改

# 打开文本文件
with open('D:\海联智通\测试\output.txt', 'r') as file:
    # 逐行读取文本文件
    for line in file:
        # 去除行末的换行符
        line = line.strip()
        # 将字符串转换为字节
        data = line.encode('utf-8')
        # 发送数据
        ser.write(data)
        # 等待一段时间，确保数据发送完成
        ser.flush()
        time.sleep(1)  # 可适当调整等待时间

# 关闭串口
ser.close()
