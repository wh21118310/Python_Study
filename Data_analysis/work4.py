import numpy as np
import csv
def get_alldata(filename):
	with open(filename,'r') as csv_file:
		col_name_all = csv_file.readline()[:-1]
		colname_str = "Clothing ID,Recommended IND,Positive Feedback Count,Class Name"
		col_name_all = col_name_all.split(",")
		colname_str = colname_str.split(",")
		colindex_lst = list()
		for colname in colname_str:
			if colname in col_name_all:
				colindex_lst.append(col_name_all.index(colname))
		dataset=[]
		for line in csv.reader(csv_file):
			data = list()
			for num in colindex_lst:
				data.append(line[num])
			dataset.append(data)
		return np.array(dataset)

def get_id_count_arr(datset):
	id_count_lst = list()
	id_count_dict = dict()
	for item in datset:
		if not item[0] in id_count_dict:
			id_count_dict[item[0]] = 1
		else:
			id_count_dict[item[0]] += 1
	for key,value in id_count_dict.items():
		if value > 400 :
			id_count_lst.append(key)
	return id_count_lst

def cal_recom_num(dataset,id_lst):
	id_recom_ratio_lst = []
	recom = dict()
	comment = dict()
	#初始化字典
	for item in id_lst:
		recom[item] = 0
		comment[item] = 0
	#字典计数
	for item in dataset:
		if item[0] in id_lst:
			recom[item[0]] += int(item[1])

			comment[item[0]] += 1
	for key1 in recom.keys():
			num = recom[key1]/comment[key1]
			id_recom_ratio_lst.append(num)
	return id_recom_ratio_lst

def cal_pos_num(dataset,id_lst):

	id_pos_sum_lst = []
	id_name_lst = []
	id_dict = dict()
	type_dict = dict()
	#字典初始化
	for item in id_lst:
		id_dict[item] = 0
	#字典赋值
	for item in dataset:
		if item[0] in id_lst:
			id_dict[item[0]] += int(item[2])
			if item[0] not in type_dict:
				type_dict[item[0]] = str(item[3])
	for item in id_dict.keys():
		id_pos_sum_lst.append(id_dict[item])
	for item in type_dict:
		id_name_lst.append(type_dict[item])
	return id_pos_sum_lst,id_name_lst

if __name__ == '__main__':
	filename = "./dataFile/womens_clothing_e-commerce_reviews.csv"
	dataset = get_alldata(filename)
	print("数据集dataset的维度是: {}".format(dataset.shape))

	# 计算评论次数大于400的唯一Clothing ID号
	id_count_lst = get_id_count_arr(dataset)
	print("评论次数大于400的唯一Clothing ID号有{}个，列表是{}".format(len(id_count_lst), id_count_lst))

	# id_data_lst：每个Clothing ID被评论的次数，id_recom_lst：每个Clothing ID被评论的推荐次数
	#     id_data_lst,id_recom_lst = cal_recom_num(dataset,id_count_lst)
	recom_ratio_lst = cal_recom_num(dataset, id_count_lst)

	# 对每个Clothing ID的服装被评论的积极反馈进行数量统计
	id_pos_sum_lst, id_name_lst = cal_pos_num(dataset, id_count_lst)

	# 将id_count_lst，id_count_lst,id_data_lst,id_recom_lst,id_pos_sum_arr进行合并
	id_data_arrs = np.array((id_count_lst, id_name_lst, recom_ratio_lst, id_pos_sum_lst)).T
	for id_data in id_data_arrs:
		print(
			"Clothing ID为 {} ,服装类型为 {},被推荐的占比为: {}，正反馈的总计数为: {}".format(id_data[0], id_data[1], id_data[2], id_data[3]))
