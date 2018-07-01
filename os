DateFrame是一个【表格型】的数据结构。DateFrame由按一定顺序排列的多列数据组成，
设计初衷是将Series的使用场景从一维拓展到多维。DataFrame既有行索引，也会有列索引

- 行索引：index
- 列索引：columns
- 值：values

1) DataFrame的创建
    - 最常用的方法是传递一个字典来创建
    例：
        dic={
        'tom':[122,132,98,78,67],
        'judy':[134,56,78,89,78]
        }
        DataFrame(data=dic)
        >>>     judy	tom
            0	134	    122
            1	56	    132
            2	78	    98
            3	89	    78
            4	78	    67

        DataFrame(data=dic,index=list('ABCDE'))
        #index为行索引，columns为列索引，
        >>>     judy	tom
            A	134	    122
            B	56	    132
            C  	78	    98
            D	89	    78
            E	78	    67

        DataFrame(data=dic,index=list('ABCDE'),columns=['java','python'])
        #当data传入的是一个字典，columns不可用，否则所有值都为None
        >>>     java	python
            A	NaN	    NaN
            B	NaN	    NaN
            C	NaN	    NaN
            D	NaN	    NaN
            E	NaN	    NaN
    DataFrame属性：values,columns,index,shape

    使用ndarray创建DataFrame：创建一个表格用于展示张三，李四，王五的java，python的成绩
    d = DataFrame(data=np.random.randint(50,100,size=[3,2]),columns=['java','python'],index=['张三','李四','王五'])
    d
    >>>     java	python
        张三	 83	      69
        李四	 81	      92
        王五	 72	      64

    DataFrame的索引
        d['java']
        #可以取得列索利的Series数组，但不可以使用行索引
        >>> 张三    83
            李四    81
            王五    72
            Name: java, dtype: int64

        d.java
        >>> 张三    83
            李四    81
            王五    72
            Name: java, dtype: int64

        d[['java','python']]
        #获取两列的数据
        >>> 	java	python
            张三	 83	      69
            李四	 81	      92
            王五	 72	      64

    行索引：
        - 使用.loc[]加index来进行行索引
        - 使用.iloc[]加整数来进行行索引

        d.loc['张三']
        >>> java      83
            python    69
            Name: 张三, dtype: int64

        d.iloc[0]
        #默认索引获取，行索引，不考虑列索引
        >>> java      83
            python    69
            Name: 张三, dtype: int64

        #张三的java成绩
        d.loc['张三']['java']
        >>> 83

        d.loc['张三','java']
        #索引的类型要一致，要么都是默认索引，要么都是实际索引值。
        #要使用默认索引值使用d.iloc[0,0]
        >>> 83

        d.iloc[0,0]
        >>> 83

    切片
        注意：
            - 索引表示的列索引
            - 切片表示的行切片

        d.loc['张三':'李四','java']
        #loc是全闭合区间
        >>> 张三    83
            李四    81
            Name: java, dtype: int64

        d.iloc[0:1,0:1]
        #不取到1，半开半闭区间
        >>>     java
            张三	 83

        d[0:1]
        #只能切行
        >>>     java	python
            张三	 83	      69


2）DataFrame的运算
        同Series运算是一样的
        - 在运算中自动补齐不同索引的数据
        - 如果索引不对应，则补NaN
        d = DataFrame(data=np.random.randint(20,40,size=(3,4)))
        d
        >>>     0	1	2	3
            0	32	22	37	24
            1	27	31	30	25
            2	33	36	38	30


        t=DataFrame(data=np.random.randint(20,40,size=(4,5)))
        t
        >>>     0	1	2	3	4
            0	33	33	24	21	38
            1	37	24	22	38	34
            2	33	35	36	27	26
            3	36	22	26	31	34

        d+t

        >>>      0	     1	     2	     3	     4
            0	65.0	55.0	61.0	45.0	NaN
            1	64.0	55.0	52.0	63.0	NaN
            2	66.0	71.0	74.0	57.0	NaN
            3	NaN	    NaN	    NaN	    NaN	    NaN

        d.add(t,fill_value=0)
        #fill_value参数会将NaN展示出来，若相加的两个数组都没有对应NaN位置的值，
        #则用fill__value的值填充，若有值，则在原来值的基础上添加fill__value的值
        >>>      0	     1	     2	     3	     4
            0	65.0	55.0	61.0	45.0	38.0
            1	64.0	55.0	52.0	63.0	34.0
            2	66.0	71.0	74.0	57.0	26.0
            3	36.0	22.0	26.0	31.0	34.0

        d-t
        >>>      0	     1	     2	     3	    4
            0	-1.0	-11.0	13.0	3.0	    NaN
            1	-10.0	7.0	    8.0	    -13.0	NaN
            2	0.0	    1.0	    2.0	    3.0	    NaN
            3	NaN	    NaN	    NaN 	NaN 	NaN


            d.sub(t,fill_value=0,axis='index')
            >>>      0	     1	     2	     3	     4
                0	-1.0	-11.0	13.0	3.0	    -38.0
                1	-10.0	7.0	    8.0	    -13.0	-34.0
                2	0.0	    1.0	    2.0	    3.0	    -26.0
                3	-36.0	-22.0	-26.0	-31.0	-34.0

            d/t
            >>>         0	        1	        2	        3	     4
                0	0.969697	0.666667	1.541667	1.142857	NaN
                1	0.729730	1.291667	1.363636	0.657895	NaN
                2	1.000000	1.028571	1.055556	1.111111	NaN
                3	NaN	        NaN	        NaN	        NaN	        NaN


            d.sum()
            #默认axis=0，计算的是列的和
            >>>  0     92
                 1     89
                 2    105
                 3     79
                 dtype: int64


            d.sum(axis=1)
            #axis=1,计算的是行的和
            >>> 0    115
                1    113
                2    137
                dtype: int64

3)pandas中的None与NaN
        1)pandas中None与np.nan都视作np.nan

        2)pandas中None与np.nan的操作

            isnull()
            notnull()
            dropna():过滤丢失数据
            fillna():填充丢失数据

        例：
             A	     B	     C	     D
        0	False	False	False	False
        1	False	True	False	True
        2	False	False	False	False

        q.isnull().any()
        #每一列的数据有True则为True，参数axis可指定行和列
        >>> A    False
            B     True
            C    False
            D     True
            dtype: bool


        q.notnull().all(axis=0)
        #每一列的数据全为True则返回True
        >>> A     True
            B    False
            C     True
            D    False
            dtype: bool

    过滤函数：重点
        q
        >>>     A	 B	    C	 D
            0	57	58.0	87	86.0
            1	52	NaN	    59	NaN
            2	82	50.0	56	99.0

        q.dropna(axis=1)
        #默认axis=0,显示行没有nan的行，axis=1，显示列没有nan的列. 与平时的axis参数是相反的
        >>>     A	C
            0	57	87
            1	52	59
            2	82	56

        q.dropna(axis=1,how='all')
        #how参数一般使用默认的any,any是全True为True，与平时使用相反
        >>>     A	 B	    C	 D
            0	57	58.0	87	86.0
            1	52	NaN	    59	NaN
            2	82	50.0	56	99.0

        q.fillna(value=100,axis=1)
        #axis无作用
        >>>     A	  B	    C	D
            0	57	58.0	87	86.0
            1	52	100.0	59	100.0
            2	82	50.0	56	99.0


        q.fillna(method='bfill',axis=1)
        #当axis=0,nan空的值由同一列的下一行的数值填充
        #当axis=1,nan空的值由同一行的后一个数值填充
        >>>      A	     B	     C	     D
            0	57.0	58.0	87.0	86.0
            1	52.0	59.0	59.0	NaN
            2	82.0	50.0	56.0	99.0


        q
        >>>     A	 B	    C	D
             0	57	58.0	87	86.0
             1	52	NaN	    59	NaN
             2	82	50.0	56	99.0


        q.fillna(method='ffill',axis=1)
        #当axis=0,nan空的值由同一列的上一行的数值填充
        #当axis=1,nan空的值由同一行的前一个数值填充
        >>>      A	     B	     C	     D
            0	57.0	58.0	87.0	86.0
            1	52.0	52.0	59.0	59.0
            2	82.0	50.0	56.0	99.0

        理综
        ddd3=DataFrame(data=np.random.randint(50,100,size=(3,4)),index=['张三','李四','王五'],columns=['语文','数学','英语','理综'])

        d3
        ddd3
        >>>     语文	数学	英语	理综
            张三	50	91	50	74
            李四	92	78	84	98
            王五	89	92	59	94

        ddd3.loc['李四','英语']=np.nan

        ddd3
        >>>     语文	数学	英语	理综
            张三	50	91	50.0	74
            李四	92	78	NaN	    98
            王五	89	92	59.0	94

        李四的英语成绩用数学填充
        ddd3.fillna(method='ffill',axis=1)
        #将李四的英语成绩用数学填充
        >>>     语文	    数学	    英语	    理综
            张三	50.0	91.0	50.0	74.0
            李四	92.0	78.0	78.0	98.0
            王五	89.0	92.0	59.0	94.0