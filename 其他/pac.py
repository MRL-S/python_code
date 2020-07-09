# n = int(input("请输入要进行多少次相加："))
# a = int(input("请输入要相加的数："))
# # total = 0
# # for i in range(1,n+1):
# #     s = 0
# #     for j in range(0,i):
# #         s += a*10**j
# #     print(s)
# #     total += s
# # print("计算和为：",total)
# from functools import reduce
# tn = 0
# sn = []
# for count in range(n):
#     tn = tn+a
#     a = a*10
#     sn.append(tn)
#     print(tn)

# sn = reduce(lambda x,y:x+y,sn)
# print("合为：",sn)
# for j in range(2,1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1,j):
#         if j % i == 0:
#             n += 1
#             s -= i
#             k.append(i)
#     if s == 0:
#         print(j)
#         for i in range(n):
#             print(str(k[i]),end=' ')
#         print(k[n])
# import math
# x = input("请输入一个不多于五位的数：")
# a = x // 10000
# b = x % 10000 // 1000
# c = x % 1000 // 100
# d = x % 100 // 10
# e = x % 10
# if a != 0:
#     print("这个数是一个五位数",e,d,c,b,a)
# elif b != 0:
#     print("是一个四位数：",e,d,c,b)
# elif c != 0:
#     print("是一个三位数：",e,d,c)
# elif d != 0:
#     print("是一个两位数：",e,d)
# else:
#     print("是一个一位数：",e)
# print(len(x))
# for i in range(len(x)):
#     print(x[i])
# if __name__ == '__main__':
#     a = [1,4,6,9,13,16,19,28,40,100,0]
#     for i in range(len(a)):
#         print(a[i])
#     number = int(input("请输入要插入的数字："))
#     end = a[len(a)-2]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(len(a)-1):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i+1,len(a)):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2
#                 break
#     for i in range(len(a)):
#         print(a[i])
# x = [[12,7,3],
#      [4,5,6],
#      [7,8,9]]

# y = [[5,8,1],
#      [6,7,3],
#      [4,5,9]]

# result = [[0,0,0],[0,0,0,],[0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         result[i][j] = x[i][j]+y[i][j]

# for r in result:
#     print(r)
# MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
# MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x
 
# if __name__ == '__main__':
#     a = 10
#     b = 20
#     print ((a>b)*a)
#     print ('The lower one is %d' % MINIMUM(a,b))
# import threading
# import time
 
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("Starting " + self.name)
#        # 获得锁，成功获得锁定后返回True
#        # 可选的timeout参数不填时将一直阻塞直到获得锁定
#        # 否则超时后将返回False
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # 释放锁
#         threadLock.release()
 
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
 
# threadLock = threading.Lock()
# threads = []
 
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
 
# # 开启新线程
# thread1.start()
# thread2.start()
 
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
 
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("Exiting Main Thread")
# import copy
# a = (11,22)
# b = (33,44)
# c = (a,b)
# e = copy.copy(c)

# d = copy.deepcopy(c)
# print(id(d),id(c))
class Test_obj(object):
    country = "China"
    def __init__(self,name,ctr):
        self.name = name
        self.country = ctr
    def Province(self):
        print(self.name)

country1 = Test_obj("山西","ruass")
country1.Province()
print(country1.country)
print(Test_obj.country)