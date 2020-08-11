import json

if __name__ == '__main__':
    # set1 = {'pid','tic','tie','tio','ano','ad','pd','pk','pno','apo','ape','apc','ipc','lc','vu','abso','abse','absc','imgtitle','imgname','lssc','pdt','debec','debeo','debee','imgo','pdfexist','ans','pns','sfpns','inc','ine','ino','agc','age','ago','asc','ase','aso','exc','exe','exo'}
    # set2 = {'vu', 'lc', 'IMGO', 'ad', 'debee', 'debeo', 'depc', 'abse', 'pk', 'ano', 'ago', 'ans', 'debec', 'ase', 'asc', 'lssc', 'pdfexist', 'cre', 'pd', 'apc', 'absoimgpath', 'cri', 'abso', 'pns', 'ine', 'crc', 'pno', 'agc', 'ipc', 'IMGNAME', 'sfpns', 'pid', 'IMGTITLE', 'exo', 'apo', 'age', 'exc', 'pdt', 'tic', 'inc', 'ino', 'cro', 'tie', 'absc', 'tio', 'pdf', 'aso', 'ape'}
    # set_sql = {'IMGTITLE','abso','tie','absc','abse','tio','inc','agc','IMGNAME','ano','tic','ans','ino','ine','IMGO','exo','pd','asc','ipc','ase','aso','exc','pk','sfpns','lssc','vu','crc','pdfexist','ape','apc','cri','apo','cro','pdt','pns','pid','pno','depc','ad','ago','pdf','age','absoimgpath','lc','debeo','debec','cre','debee'}
    # print(set1 - set2)
    # print(set2 - set1)
    # print(set1 & set2)
    # print(len(set1 | set2))
    #
    # print(set_sql - set2)
    # print(set_sql - set1)

    table_header = {'imgtitle', 'abso', 'tie', 'absc', 'abse', 'tio', 'inc', 'agc', 'imgname', 'ano', 'tic', 'ans',
                    'ino', 'ine', 'imgo', 'exo', 'pd', 'asc', 'ipc', 'ase', 'aso', 'exc', 'pk', 'sfpns', 'lssc', 'vu',
                    'crc', 'pdfexist', 'ape', 'apc', 'cri', 'apo', 'cro', 'pdt', 'pns', 'pid', 'pno', 'depc', 'ad',
                    'ago', 'pdf', 'age', 'absoimgpath', 'lc', 'debeo', 'debec', 'cre', 'debee'}
    field_name = {'imgtitle', 'abso', 'absoimgpath', 'tie', 'absc', 'abse', 'tio', 'inc', 'agc', 'imgname', 'ano',
                  'tic', 'ans', 'ino', 'ine', 'imgo', 'exo', 'pd', 'pdt', 'pdfexist', 'pdf', 'asc', 'ipc', 'ase', 'aso',
                  'exc', 'sfpns', 'lssc', 'vu', 'crc', 'pdfexist', 'ape', 'apc', 'cri', 'apo', 'cro', 'pdt', 'pns',
                  'sfpns', 'pid', 'pno', 'depc', 'ad', 'add_time', 'ago', 'pdfexist', 'pdf', 'age', 'absoimgpath', 'lc',
                  'debeo', 'debec', 'cre', 'debee'}
    field_name_l = ['imgtitle', 'abso', 'absoimgpath', 'tie', 'absc', 'abse', 'tio', 'inc', 'agc', 'imgname', 'ano', 'tic', 'ans',
     'ino', 'ine', 'imgo', 'exo', 'pd', 'pdt', 'pdfexist', 'pdf', 'asc', 'ipc', 'ase', 'aso', 'exc', 'sfpns', 'lssc',
     'vu', 'crc', 'pdfexist', 'ape', 'apc', 'cri', 'apo', 'cro', 'pdt', 'pns', 'sfpns', 'pid', 'pno', 'depc', 'ad',
     'add_time', 'ago', 'pdfexist', 'pdf', 'age', 'absoimgpath', 'lc', 'debeo', 'debec', 'cre', 'debee']

    print(table_header - field_name)
    print(field_name - table_header)
    print(len(table_header), len(field_name))
    print(len(field_name_l))

    from collections import Counter  # 引入Counter

    field_name_a = field_name_l
    field_name_b = dict(Counter(field_name_l))
    print([key for key, value in field_name_b.items() if value > 1])  # 只展示重复元素
    print({key: value for key, value in field_name_b.items() if value > 1})  # 展现重复元素和重复次数