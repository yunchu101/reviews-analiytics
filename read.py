data = []
count = 0

with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count+1
		if count % 1000 == 0 :
			print(len(data))
print ('finish reading total are', len(data),'line data')

sum_len = 0
for d in data:
	sum_len = sum_len+len(d)
print(sum_len)
print(sum_len/len(data))

