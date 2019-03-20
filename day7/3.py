# 
# Base64是一种用64个字符来表示任意二进制数据的方法。

import base64

print( base64.b64encode(b'binary\x00string') )

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

print( base64.b64encode(b'i\xb7\x1d\xfb\xef\xff') )

print(  base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff') )

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

print("====================================================================")


# struct
'''
    准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。
    而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。

    在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：

    好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
'''
import struct

st = struct.pack('>I',10240099)
print( st )

'''
    pack的第一个参数是处理指令，'>I'的意思是：

    >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

    后面的参数个数要和处理指令一致。
'''

# unpack把bytes变成相应的数据类型：

n = struct.unpack('>I',b'\x00\x9c@c')

print( n )


# hashlib提供了常见的摘要算法，如MD5，SHA1等等。

import hashlib

md5 = hashlib.md5()
md5.update("this is my first time , what are you saying  ?".encode("utf-8"))
print(md5.hexdigest())


'''
    MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

    另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
'''

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

'''
    SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

    比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
'''



# hmac
import hmac

message = b'Hello , world'
key = b'secret'
h = hmac.new( key, message, digestmod='MD5' )
print( h.hexdigest() )
'''
    可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。
    需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
'''
