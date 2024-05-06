import serial
import time

def send_data_via_serial(data, serial_port):
    # 打开串口
    ser = serial.Serial(serial_port)
    # 发送数据
    ser.write(data)
    # 关闭串口
    ser.close()

def convert_to_byte_array(line):
    # 移除换行符并分割字符串
    hex_values = line.strip().split()
    # 将十六进制字符串转换为整数列表
    int_values = [int(value, 16) for value in hex_values]
    # 将整数列表转换为字节数组
    byte_array = bytes(int_values)
    return byte_array

def wait_for_response(serial_port):
    # 打开串口
    ser = serial.Serial(serial_port)
    # 读取串口数据
    response = ser.read(1)
    # 关闭串口
    ser.close()
    return response

def main(file_path, serial_port):
    # 打开文件
    with open(file_path, 'r') as file:
        # 逐行读取文件内容
        for line in file:
            # 转换成字节数组
            byte_array = convert_to_byte_array(line)
            # 通过串口发送数据
            send_data_via_serial(byte_array, serial_port)
            # 等待回复
            response = wait_for_response(serial_port)
            # 如果有回复，等待时间设为0，否则等待10毫秒
            wait_time = 0 if response else 0.01
            # 等待一段时间再发送下一条数据
            time.sleep(wait_time)

if __name__ == "__main__":
    file_path = "D:\海联智通\测试\output.txt"  # 替换成你的文件路径
    serial_port = "com4"  # 替换成你的串口名称
    main(file_path, serial_port)