import gdb

class GdbServer():
    fileName = 'demo'

    def __init__(self):
        print('GdbServer init')

    def start(self):
        print('=========> come in the start')
        ret1 = gdb.execute('file demo', to_string=True)
        print('(gdb server) file demo:\n' + ret1)
        ret2 = gdb.execute('start', to_string=True)
        print('(gdb server) start:\n' + ret2)
        return 'file command return: ' + ret1 + '\nstart command return: ' + ret2

    def contin(self):
        print('=========> come in the contin')
        ret_str = gdb.execute('c', to_string=True)
        print('(gdb server) continue:\n' + ret_str)
        return 'continue result:' + ret_str