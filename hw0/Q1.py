# coding=gbk
# ���հ�
# �ֵ��Զ�Ѱ���������ʽ������ӵ�й̶�˳�����б����ϣ�����Ԫ��
# ���ǣ�������������һ�ַ�������dict��val�����ټ�һ���word����dict��˳��Order��;
# ���ǰ����dict��һ����Order�������еĲ���
class word_Node(object):
    def __init__(self, order, count):
        self.order = order
        self.count = count

def calcularte_word(srcName,dstName):
    src = load_txt(srcName)
    # print(src)
    # --------------------------------------------------------------
    # ���Ĵ��룺hashmapԭ����sΪkey��ɨ��src��ͳ��ÿ��s�ĳ��ִ���
    finded_dict = {} # ����ѷ��ֵ�word���䡾Node:����˳������ִ�����
    # count_list = [] # ����Ѽ���finded_dict��word�ĳ��ִ���
    order = 0 # ˳��Ϊ0
    for s in src:
        if finded_dict.get(s) is None: # o(1)���������Ӷ� {s��һ�η���}
            node = word_Node(order, 1) # count��Ϊ1
            order = order + 1 # Ϊ�¸��ڵ�����order
            finded_dict[s] = node # s����finded_dict��ֵ����������finded_dict��˳��{ָ����s��src��ԭ˳��}��count
        else:
            finded_dict[s].count = finded_dict[s].count + 1 # count��һ
    # ---------------------------------------------------------------
    res_list = sorted(finded_dict.items(), key=lambda item:(item[1].order)) # ���ݵڶ����ֶ�
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
# # �����ǣ�
# # �ֵ��Զ�Ѱ���������ʽ
# # ����ӵ�й̶�˳�����б����ϣ�����Ԫ��
# # �ұ���Ҫ{����ԭ������˳��} �����
# def calcularte_word(srcName,dstName):
#     src = load_txt(srcName)
#     # --------------------------------------------------------------
#     # ���Ĵ��룺hashmapԭ����sΪkey��ɨ��src��ͳ��ÿ��s�ĳ��ִ���
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
# # �����ǹ���ʵ�ֵ�demo_1
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
# # ����ִ��
# if __name__ == '__main__':
#     # test_func_test()
#
#     # test_load_txt()
#
#     # test_storage_txt()
#
# # ------------------------------------------------------------------------------------------------


