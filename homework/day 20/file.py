# # try:
# #     flie = open('flie', 'mode')
# #     data = flie.read()
# # except IOError:
# #     pass
# # finally:
# #     if  flie:
# #         f.close()
# # with open(flie,'mode') as f:
# #     f.read()
# #
# # with open('test.txt', 'a',encoding = 'utf - 8') as fw:
# #
# #     # name = input('请输入名字')
# #     # fw.write(name)
# #     li = ['hello world',' python']
# #     fw.writelines(li)
# import os
#
# if __name__ == '__main__':
#     print(os.name)
#     # print(os.environ)
#     print(os.curdir)
#     print(os.getcwd())
#     path = 'C:\homework\day 20'
#     print(os.listdir(path))
#     # print(os.mkdir('name'))
#     # print(os.makedirs('homeworks'))
#     # print(os.rmdir('homeworks'))
#     print(os.rmdir('python'))
#     print(os.walk())

# import shutil
# with open('english.txt', 'r', encoding = 'utf- 8') as file:
#     data = file.readlines()
#     year = input('请输入年份:\n')
#     for na in data:
#         if year in na:
#             print(na)
#             break
#         else:
#             print('这一年没有举办!')

# with open('xiaoming.txt', 'a',encoding = 'utf - 8') as fw, open('xiaohong.txt', 'a', encoding = 'utf - 8') as fn:
#     flga = True
#     while flga:
#         xm_write = fw.writelines(input('小明说:\n'))
#         if xm_write == 'bye':
#             break
#         print(xm_write , '+ ','\n')
#         fw.flush()
#         xh_write = fn.writelines(input('小红说:\n'))
#         print(xh_write, '+', '\n')
#         fn.flush()
# with open(r'C:\summarizing\every work\t0152110622c075b9db.jpg', 'rb') as imp,open('new.png', 'wb') as fwb:
#     frb_png = imp.read()
#     fwb.write(frb_png)
#     fwb.flush
# from socket import *
# udp_socket = (AF_INET, SOCK_DGRAM)
# host = '192.168.52'
# port = 9090
# address = (host, port)
# byte = 1 * 1024
# while True:
#     data = input('请输入内容:\n')
#     if not data:
#         break
#     udp_socket.sendto(data.encode('utf-8'), address)
#
#     print(udp_socket.close())
from socket import *
host = 'localhost'#客户端准备连接的服务器的地址
port = 10000#服务器的端口号
address = (host, port)#服务器的地址

bufsize = 1024 #客户端缓冲区的大小(单位字节)
tcp_socket = socket(AF_INET,SOCK_STREAM)#所有的套接字都使用socket 函数来创建
tcp_socket.connect(address)#客户端去连接服务器

while True:
    data = input('>')#从键盘读取数据
    if not data:
        break
        #给服务器发送消息,由于 send 只能发送字节数据,所以把字符串编码之后再发送
    tcp_socket.send(data.encode('utf-8'))

    data = tcp_socket.recv(bufsize)#