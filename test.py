# coding:utf-8

#
# months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
#           'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
#
#
# def split_months(time):
#     l = time.split('-')
#     l[1] = str(months[l[1]])
#     o = l[0]
#     l[0] = '20' + l[2]
#     l[2] = o
#     print(l)
#     print('-'.join(l))
#     return '-'.join(l)
#
#
# f=[1,2,3,-1,-3,-4,0,3,7,-9]
# t=sorted(f,key=lambda x:(x<0),reverse=True)
# print(t)
# # if __name__ == '__main__':
# #     split_months('01-AUG-11')
#
#
# t=sorted('dsdf23c2DFGT23sc3',key=lambda x: (x.isdigit(),x.isdigit() and int(x)%2==0,x.isupper(),x))
#
# print(t)
#
# a=[1,3,5,7,9]
# b=[2,4,6,8,10]
# #将a和b列表合并，生成c列表，且c列表有序
#
# def c_list(a,b):
#     n=len(a)
#     m=len(b)
#     i=j=0
#     c=[]
#     while i<n and j<m:
#         if a[i]<b[j]:
#             c.append(a[i])
#             i+=1
#         elif a[i]>b[j]:
#             c.append(b[j])
#             j+=1
#         else:
#             c.append(a[i]*2)
#             i+=1
#             j+=1
#
#     if i<n:
#         c.extend(a[i:])
#     elif j<m:
#         c.extend(b[j:])
#     return c
#
# if __name__ == '__main__':
#     print(c_list(a,b))


#ls,pwd,cp,mkdir,echo,tree,grep,ps,rm,who,cat,cd,vi,sudo,
#ln,source,kill,help,su
#
#
# class A(object):
#     age=10
#     def __init__(self,name='wu'):
#         self.name=name
#     def obj(self):
#
#         print('aaaa')
#     # def __repr__(self):
#     #     print('wu')
#     @classmethod
#     def class_uuu(cls):
#         cls.age=20
#
#         print('dddddd')
#
#     @staticmethod
#     def hhh(obja,ddd):
#
#         print('ssssss',obja.name,ddd)
#
#
# if __name__ == '__main__':
#     a=A()
#     A.hhh(a,'ooo')
#     a.hhh(a,'ooo')
#     A.class_uuu()


# import csv
#
# with open('hello.csv','a+') as f:
#     write=csv.writer(f)
#     write.seek(0)
#     write.writerow(['ddd','ttt','ww','eee'])

# import collections
#
# d=[1,2,3,4,4,2,3]
#
# t=collections.Counter(d)
# print(t)
# print(type(t))
# for i,y in t.items():
#
#     print(i,y)

def sum(num):
    a,b=0,1
    l=[]
    l.append(a)
    l.append(b)
    c=2
    while c<num:
        a,b=b,a+b
        l.append(b)
        c+=1
    print(l)

if __name__ == '__main__':
    sum(10)