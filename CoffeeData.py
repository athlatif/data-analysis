with open('coffee-preferences.csv','r') as f:
    
    lines = f.readlines()
    
    print("\n ###### Data before cleaning ###### \n ")
    print(lines)
    
    cleaned_lines = []
for l in lines:
    cleaned_lines.append(l.replace('\n',''))

header = cleaned_lines[0]
data = cleaned_lines[1:]

header = header.split(',')


split_data = []
for d in data:
    split_data.append(d.split(','))

# Remove Timestamp:
header = header[1:]

data_nots = []
for row in split_data:
    data_nots.append(row[1:])

    #print(data_nots)  




i = 0
z = 0.0
j = 0

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

vals = [] 

for row in data_nots:
    newrow = []
    for elm in row:
        if RepresentsInt(elm) == False and elm != '':
            newrow.append(elm)
        else:
            if RepresentsInt(elm):
                z = float(elm)
                newrow.append(z)
            if elm == '':
                newrow.append("None")
                
    vals.append(newrow) 

print("\n ###### Data after cleaning ###### \n ")
print(vals)


print("\n ###### number of None per person  ###### \n ")
      
      
dic = {}
num = 0
i=0
for row in data_nots:
    newrow = []
    num = 0
    for elm in row:
        if RepresentsInt(elm) == False and elm != '':
            newrow.append(elm)
            i = i + 1
        else:
            if elm == '':
                num = num + 1
            dic[newrow[0]] = num
      
print(dic)     


print("\n ###### Avrage per coffee brand  ###### \n ")
      
data_num = []
average_rating = 0
rating = {}

for h in header[1:]:
  rating[h] = []
  
  
for row in data_nots:
    for i, col in enumerate(row):
        if i > 0 and col != '':
            rating[header[i]].append(col)
 
avrage = {}    

for i,rate in rating.items():

    for w in range(len(rate)):
        rate[w] = int(rate[w])
    average_rating = float(sum(rate))/len(rate)  
    avrage[i] = average_rating
    

print(avrage)


        
    
    
