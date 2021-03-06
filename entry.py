import socket
import sys
sys.path.append('./')

from gdbServer import GdbServer

# TCP服务端
def main():

    #创建一个socket对象，AF_INET指定使用IPv4协议(AF_INET6代表IPV6)，SOCK_STREAM指定使用面向流的TCP协议
    tcp_serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_serve_socket.bind(('localhost', 8001))   # 绑定本地ip和端口
    tcp_serve_socket.listen(128)                # 开始监听端口，数字表示等待连接的最大数量

    gdbSer = GdbServer()

    # 循环目的：多次调用accept为多个客户服务
    while True:
        print('等待一个新请求到来....')
        tcp_client_socket, client_addr = tcp_serve_socket.accept()
        print('一个新请求到来，来自：%s' % str(client_addr))

        recv_data = tcp_client_socket.recv(1024).decode('utf-8')   # 从客户端接受消息，最多1024字节。recv_data为字节类型，.decode()将recv_data转化成字符型
        print('请求发送的命令是%s' % recv_data)

        retMsg = ''
        if recv_data == 'start':
            print('send start to gdb')
            retMsg = gdbSer.start()
        elif recv_data == 'continue':
            print('send continue to gdb')
            retMsg = gdbSer.contin()
        else:
            print('no this commond')
        print(retMsg)

        tcp_client_socket.send(retMsg.encode('utf-8'))	# 将字符串进行字节编码

        # 关闭与客户端的连接
        tcp_client_socket.close()
        print('请求响应完毕')

    del gdbSer
    tcp_serve_socket.close()

if __name__ == '__main__':
    main()
