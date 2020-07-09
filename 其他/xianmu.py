# import csv
# with open('assets.csv', 'a', newline='') as csvfile:
# #调用open()函数打开csv文件，传入参数：文件名“assets.csv”，、追加模式“a”、newline=''。
#     writer = csv.writer(csvfile, dialect='excel')
#     # 用csv.writer()函数创建一个writer对象。
#     header = ['小区名称','地址', '建筑时间','楼栋', '单元',  '门牌', '朝向', '面积']
#     # 用writerow()函数将表头写进csv文件
#     writer.writerow(header)
start_floor = '3'
end_floor = '4'
floor_last_number = ['01','02','03']
# 户室的尾号

start_floor_rooms = {301:[1,80], 302:[1,80], 303:[2,90]}
#初始楼层的模版数据

unit_rooms={}
#创建一个字典
unit_rooms[int(star_floor)] = start_floor_rooms
i = int(start_floor)+1
j = 0
for i <= int(end_floor):
    room_info = {}
    for j < len(floor_last_number):
        number = str(i)+floor_lart_number[j]
        info  = start_floor_rooms[start_floor+floor_last_number[j]]
        room_info[int(number)] = info
        unit_rooms[i] = room_info
       