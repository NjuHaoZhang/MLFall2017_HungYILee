# coding=gbk
# 最终版
# 字典自动寻找最佳排序方式，如想拥有固定顺序，用列表，集合，或者元组
# 但是，我这里用了另一种方法：在dict的val里面再加一项，【word加入dict的顺序Order】;
# 输出前，对dict做一个按Order升序排列的操作
class word_Node(object):
    def __init__(self, order, count):
        self.order = order
        self.count = count

def calcularte_word(srcName,dstName):
    src = load_txt(srcName)
    # print(src)
    # --------------------------------------------------------------
    # 核心代码：hashmap原理，以s为key，扫描src，统计每个s的出现次数
    finded_dict = {} # 存放已发现的word及其【Node:包括顺序与出现次数】
    # count_list = [] # 存放已加入finded_dict的word的出现次数
    order = 0 # 顺序为0
    for s in src:
        if finded_dict.get(s) is None: # o(1)的搜索复杂度 {s第一次发现}
            node = word_Node(order, 1) # count记为1
            order = order + 1 # 为下个节点生成order
            finded_dict[s] = node # s放入finded_dict，值就是它加入finded_dict的顺序{指代了s在src的原顺序}及count
        else:
            finded_dict[s].count = finded_dict[s].count + 1 # count加一
    # ---------------------------------------------------------------
    res_list = sorted(finded_dict.items(), key=lambda item:(item[1].order)) # 根据第二个字段
    # print(res_list)
    storage_result(dstName, res_list)

def load_txt(filename):
    data = []
    with open(filename, 'r') as f:
        all = f.readlines()
        for line in all:
            tmp = line.split()
        data = data + tmp
    return data

def storage_result(dstName, res_list):
    with open(dstName, 'w') as f:
        for index, key in enumerate(res_list):
            # print(index, ' ', key[0], ' ', key[1].count)
            line = str(index)+ ' ' + key[0] + ' ' + str(key[1].count) + '\n'
            f.write(line)


if __name__ =="__main__":
    srcName, dstName = 'words.txt', 'Q1.txt'
    calcularte_word(srcName, dstName)

# # demo_2
# # 问题是：
# # 字典自动寻找最佳排序方式
# # 如想拥有固定顺序，用列表，集合，或者元组
# # 我必须要{保持原有输入顺序} 来输出
# def calcularte_word(srcName,dstName):
#     src = load_txt(srcName)
#     # --------------------------------------------------------------
#     # 核心代码：hashmap原理，以s为key，扫描src，统计每个s的出现次数
#     hashTable = {}
#     for s in src:
#         if hashTable.get(s) is None:
#             hashTable[s] = 1
#         else:
#             hashTable[s] = hashTable[s] + 1
#     # ---------------------------------------------------------------
#     storage_result(dstName, hashTable)
#
# def load_txt(filename):
#     data = []
#     with open(filename, 'r') as f:
#         all = f.readlines()
#         for line in all:
#             tmp = line.split()
#         data = data + tmp
#     return data
#
# def storage_result(dstName, hashTable):
#     with open(dstName, 'w') as f:
#         for index, key in enumerate(hashTable):
#             line = str(index)+ ' ' + key + ' ' + str(hashTable[key]) + '\n'
#             f.write(line)
#
#
# if __name__ =="__main__":
#     srcName, dstName = 'words.txt', 'Q1.txt'
#     calcularte_word(srcName, dstName)
# # ----------------------------------------------------------------------------------------

# # --------------------------------------------------------------------------------------
# # 下面是功能实现的demo_1
# def func_test():
#     src = ['a', 'b', 'b', 'c', 'a', 'd', 'c', 'c']
#     # 'a' 0 2
#     # 'b' 1 2
#     # 'c' 2 3
#     # 'd' 3 1
#     # print( list(range(len(src))) )
#     hashTable = {}
#     num = []
#     for s in src:
#         if hashTable.get(s) is None:
#             hashTable[s] = 1
#         else:
#             hashTable[s] = hashTable[s] + 1
#     print(type(hashTable), ' ', hashTable)
#     for index, key in enumerate(hashTable):
#         print(index, key, hashTable[key])
#
# def test_func_test():
#     func_test()
#
# def load_txt(filename):
#     data = []
#     with open(filename, 'r') as f:
#         all = f.readlines()
#         for line in all:
#             tmp = line.split()
#         data = data + tmp
#     return data
#
# def test_load_txt():
#     filename = 'words.txt'
#     data = load_txt(filename)
#     print(data)
#
# def storage_txt(filename):
#     with open(filename, 'w') as f:
#         f.write('Hello, world 1!\n')
#         f.write('Hello, world 2!\n')
#         f.write('Hello, world 3!\n')
#
# def test_storage_txt():
#     filename = r"test.txt"
#     storage_txt(filename)
#     with open(filename, 'r') as f:
#         for fp in f:
#             print(fp)
#
#
# # 调用执行
# if __name__ == '__main__':
#     # test_func_test()
#
#     # test_load_txt()
#
#     # test_storage_txt()
#
# # ------------------------------------------------------------------------------------------------


