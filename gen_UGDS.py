# coding: utf-8
import csv
def handlUGDSMAN():
	dic = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic2 = {"AL":"Alabama","AK":"Alaska","AR":"Arkansas","AZ":"Arizona","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","IA":"Iowa","ID":"Idaho","IL":"Illinois","IN":"Indiana","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","MA":"Massachusetts","ME":"Maine","MD":"Maryland","MI":"Michigan","MN":"Minnesota","MO":"Missouri","MS":"Mississippi","MT":"Montana","NE":"Nebraska","NC":"North Carolina","ND":"North Dakota","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NV":"Nevada","NY":"New York","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","DC":"District of Columbia","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"   ,"AS":"0","GU":"0","MP":"0","PR":"0","FM":"0","PW":"0","VI":"0","MH":"0"}
	csvfile = file('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb')
	reader = csv.reader(csvfile)
	flag = 0;
	for line in reader:
		'''
		for i in range(len(line)):
			if line[i] == "UGDS_MEN":
				print i
				break
		'''
		# state 5 UGDSMAN 1739 UGDSWOMEN 1740
		if(flag == 0):
			flag = 1
			continue
		if line[1739] == "NULL":
			dic[line[5]] = dic[line[5]] + 0.0
		else:
			dic[line[5]] = dic[line[5]] + float(line[1739])
	print dic
	csvfile.close();
	fp = open(r'UGDSMAN.csv', 'w')
	for key in dic:
		if dic2[key] != "0":
			strs = dic2[key]+","+str(dic[key]) + "\n"
			fp.write(strs)
	fp.close()
def handlUGDSWOM():
	dic = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic2 = {"AL":"Alabama","AK":"Alaska","AR":"Arkansas","AZ":"Arizona","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","IA":"Iowa","ID":"Idaho","IL":"Illinois","IN":"Indiana","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","MA":"Massachusetts","ME":"Maine","MD":"Maryland","MI":"Michigan","MN":"Minnesota","MO":"Missouri","MS":"Mississippi","MT":"Montana","NE":"Nebraska","NC":"North Carolina","ND":"North Dakota","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NV":"Nevada","NY":"New York","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","DC":"District of Columbia","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"   ,"AS":"0","GU":"0","MP":"0","PR":"0","FM":"0","PW":"0","VI":"0","MH":"0"}
	csvfile = file('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb')
	reader = csv.reader(csvfile)
	flag = 0;
	for line in reader:
		'''
		for i in range(len(line)):
			if line[i] == "UGDS_MEN":
				print i
				break
		'''
		# state 5 UGDSMAN 1739 UGDSWOMEN 1740
		if(flag == 0):
			flag = 1
			continue
		if line[1739] == "NULL":
			dic[line[5]] = dic[line[5]] + 0.0
		else:
			dic[line[5]] = dic[line[5]] + float(line[1740])
	print dic
	csvfile.close();
	fp = open(r'UGDSWOM.csv', 'w')
	for key in dic:
		if dic2[key] != "0":
			strs = dic2[key]+","+str(dic[key]) + "\n"
			fp.write(strs)
	fp.close()
def handlSCHDEG():
	dic = {"1":0, "2":0,"3":0,"NULL":0}
	csvfile = file('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb')
	reader = csv.reader(csvfile)
	flag = 0;
	#SCH_DEG 10
	num = 10;
	for line in reader:
		if(flag == 0):
			flag = 1
			continue
		dic[line[num]] = dic[line[num]] + 1
	print dic
	csvfile.close();
	fp = open(r'SCHDEG.csv', 'w')
	for key in dic:
		strs = key+","+str(dic[key]) + "\n"
		fp.write(strs)
	fp.close()
def handlPREDDEG():
	dic = {"0":0,"1":0, "2":0,"3":0,"4":0}
	csvfile = file('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb')
	reader = csv.reader(csvfile)
	flag = 0;
	#SCH_DEG 10
	num = 14;
	for line in reader:
		if(flag == 0):
			flag = 1
			continue
		dic[line[num]] = dic[line[num]] + 1
	print dic
	fp = open(r'PREDDEG.csv', 'w')
	for key in dic:
		strs = key+","+str(dic[key]) + "\n"
		fp.write(strs)
	fp.close()
def handlCDR3():
	dic = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic1 = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic2 = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	csvfile = file('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb')
	reader = csv.reader(csvfile)
	flag = 0;
	for line in reader:
		'''
		for i in range(len(line)):
			if line[i] == "UGDS_MEN":
				print i
				break
		'''
		# state 5 UGDSMAN 1739 UGDSWOMEN 1740
		if(flag == 0):
			flag = 1
			continue
		if line[1741] == "NULL":
			dic[line[5]] = dic[line[5]] + 0.0
			dic1[line[5]] = dic1[line[5]] + 0
		else:
			dic[line[5]] = dic[line[5]] + float(line[1741])
			dic1[line[5]] = dic1[line[5]] + 1
	print dic
	for i in dic:
		try:
			dic[i] = dic[i]/dic1[i]	
		except :
			dic[i] = 0
	csvfile.close();
	fp = open(r'CDR3.csv', 'w')
	for key in dic:
		strs = key+","+str(dic[key]) + "\n"
		fp.write(strs)
	fp.close()
def handlCDR2():
	dic = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic1 = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic2 = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	csvfile = file('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb')
	reader = csv.reader(csvfile)
	flag = 0;
	for line in reader:
		'''
		for i in range(len(line)):
			if line[i] == "UGDS_MEN":
				print i
				break
		'''
		# state 5 UGDSMAN 1739 UGDSWOMEN 1740
		if(flag == 0):
			flag = 1
			continue
		if line[1742] == "NULL":
			dic[line[5]] = dic[line[5]] + 0.0
			dic1[line[5]] = dic1[line[5]] + 0
		else:
			dic[line[5]] = dic[line[5]] + float(line[1742])
			dic1[line[5]] = dic1[line[5]] + 1
	print dic
	for i in dic:
		try:
			dic[i] = dic[i]/dic1[i]	
		except :
			dic[i] = 0
	csvfile.close();
	fp = open(r'CDR2.csv', 'w')
	for key in dic:
		strs = key+","+str(dic[key]) + "\n"
		fp.write(strs)
	fp.close()
def handlCDR2():
	dic = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic1 = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	dic2 = {"AL":0,"AK":0,"AR":0,"AZ":0,"CA":0,"CO":0,"CT":0,"DE":0,"FL":0,"GA":0,"HI":0,"IA":0,"ID":0,"IL":0,"IN":0,"KS":0,"KY":0,"LA":0,"MA":0,"ME":0,"MD":0,"MI":0,"MN":0,"MO":0,"MS":0,"MT":0,"NE":0,"NC":0,"ND":0,"NH":0,"NJ":0,"NM":0,"NV":0,"NY":0,"OH":0,"OK":0,"OR":0,"PA":0,"RI":0,"SC":0,"SD":0,"TN":0,"TX":0,"UT":0,"VT":0,"VA":0,"WA":0,"DC":0,"WV":0,"WI":0,"WY":0   ,"AS":0,"GU":0,"MP":0,"PR":0,"FM":0,"PW":0,"VI":0,"MH":0}
	csvfile = file('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb')
	reader = csv.reader(csvfile)
	flag = 0;
	for line in reader:
		'''
		for i in range(len(line)):
			if line[i] == "UGDS_MEN":
				print i
				break
		'''
		# state 5 UGDSMAN 1739 UGDSWOMEN 1740
		if(flag == 0):
			flag = 1
			continue
		if line[1742] == "NULL":
			dic[line[5]] = dic[line[5]] + 0.0
			dic1[line[5]] = dic1[line[5]] + 0
		else:
			dic[line[5]] = dic[line[5]] + float(line[1742])
			dic1[line[5]] = dic1[line[5]] + 1
	print dic
	for i in dic:
		try:
			dic[i] = dic[i]/dic1[i]	
		except :
			dic[i] = 0
	csvfile.close();
	fp = open(r'CDR2.csv', 'w')
	for key in dic:
		strs = key+","+str(dic[key]) + "\n"
		fp.write(strs)
	fp.close()
print("USGSMAN")
handlUGDSMAN()
print("UGDSWOM")
handlUGDSWOM()
print("SCHDEG")
handlSCHDEG()
print("PREDDEG")
handlPREDDEG()
print("CDR3")
handlCDR3()
print("CDR2")
handlCDR2()