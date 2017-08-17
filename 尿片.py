#encoding:utf-8
import math

#专供日亚使用
#日亚购物价格计算
#日元兑换人民币价格（百度数据）
riyuanzhuanrenmingbi = 0.0621
#运费计算函数
def yunfeijisuan(zhongliang):
	zhongliang = math.ceil(zhongliang)
	riyuanyunfei = 0
	if zhongliang <= 1:
		riyuanyunfei = 1600
	elif zhongliang <= 10:
		riyuanyunfei = 1600 + ((zhongliang - 1) * 300)
	elif zhongliang <= 20:
		riyuanyunfei = 4300 + ((zhongliang - 10) * 250)
	riyuanyunfei += 150 #不计算合箱的情况下，手续费150日元
	return riyuanyunfei * riyuanzhuanrenmingbi

###########################以上数据禁止改动##################################



#计算时，修改重量、价格、折扣和数量

#重量
zhongliang = 6
#商品价格
shangpingjiage = 5500
#商品数量（如果计算尿片每片价格，请输入每包片数）
shangpinshuliang = 208
#折扣(针对某商品打几折，1表示不打折，0.5表示打5折)
zhekou = 1
#立减(买满多少钱立减多少，可填在下方)
lijian = 0

#############################################################################


shangpingjiage = shangpingjiage - lijian

#商品人民币价格
rmbprice = shangpingjiage * zhekou * riyuanzhuanrenmingbi  / shangpinshuliang

#总价格（运费+商品价格）
allprice = yunfeijisuan(zhongliang) + shangpingjiage * riyuanzhuanrenmingbi

print ("计算公式汇率基数")
print ("10000日元=%f\n"%(10000 * riyuanzhuanrenmingbi))

print ("商品重量=%fKG"%(zhongliang))

print ("海运运费=%f\n"%(yunfeijisuan(zhongliang)))

print ("商品总价=%f"%(shangpingjiage * riyuanzhuanrenmingbi))

print ("商品单价=%f\n"%(rmbprice))

print ("总价格=%f\n"%(allprice))
