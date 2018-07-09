
import uuid

import hashlib

def md5_encode(data):
    #调用md5算法,用一个变量接收
    m = hashlib.md5()
    #调用update对传来的data进行数据加密,encode utf-8的编码后才能用update
    m.update(data.encode('utf-8'))
    return m.hexdigest() #经过特殊处理之后以字符串形式返回

res = md5_encode("cmr")
print(len(res))



