import serial
serialObj = serial.Serial('COM4')
print(serialObj)
serialObj.close()













# import serial
# from serial import Serial
#
# ser = serial.Serial('COM5', 19200)
# data = ser.readline(1000)
# print ("data")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # import socket
# # # import subprocess
# # # import serial
# # # from contextlib import closing
# # #
# # #
# # # def check_socket(host, port):
# # #     subprocess.call('C:\\device manager')
# # #     ser = serial.Serial("COM4")  # Open named port
# # #     ser.baudrate = 19200
# # #     with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
# # #         result = sock.connect_ex(('172.30.26.54', 80))
# # #         if sock.connect_ex((host, port)) == 0:
# # #             print("Port is open")
# # #         else:
# # #             print("Port is not open")
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # import socket
# # import subprocess
# # import serial
# # def check_socket(host, port):
# #   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #   subprocess.call('Control Panel')
# #   ser = serial.Serial("COM5")  # Open named port
# #   ser.baudrate = 19200
# #   result = sock.connect_ex(('172.30.26.54',80))
# #   if result == 0:
# #     print("Port is open")
# #   else:
# #     print("Port is not open")
# #     sock.close()