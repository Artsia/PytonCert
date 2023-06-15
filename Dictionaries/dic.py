#Syntax Diff. between arrays, lists, tuples, and dictionarys
#https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/dictionaries-and-loops
 
    

names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']


def my_names(names):
    d = dict()
    for name in names:
        if name not in d:
            d[name] = 1  # assign this value with an initail key of 1 into the dictionary
        else:
            # update dictionary key for that name by 1
            d[name] = d[name] + 1
    return d


new_dic = my_names(names)
#print(new_dic)


def _count_words():
    count = dict()
    file_ref = open("words.txt", "rt") # create file object
    r = file_ref.read().split()
    
    for word in r:
     count[word] = count.get(word,0) + 1
    print("Counted: ", count)
    

dic = {"aron":21, "betty":46, "sam":36, "phillip": 23} 
#key are in qoutes , values after colon methods dic.keys(), dic.values()
n = list()
i = 0
for key in dic:
    n.append(dic[key])
    #print("ages: ", n[i])
    i = i + 1
#print(" keys: ", dic.keys())
#print(" keys: ", dic.values())

#result as tuple -collection of objs separated by commas. 
#print(dic.items())
#Each key and value pair in a dictionary results in 1 tubple

#Tuples: same as list but uses () and are immutable but a list uses [] and is mutable.


names = ('csev', 'cwen', 'csev', 'zqian', 'cwen')

(a,b,c) = (1,2,3)
#print(a)


#Comparing and sorting tuples

d = {"aron":21, "betty":46, "sam":36, "phillip": 23}
List = sorted(d.items(),reverse=True) #List containing sorted tuples reversed

# create a list
l =  list()
for k,v in List:
    l.append((v,k) )

#print(l)

#same as code below
#print( sorted( [ (k,v) for k,v in d.items() ], reverse=True ) )
#REGLAR EXPRESSIONS



#nETWORKS
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'data.pr4e.org'
port = 80
mysocket.connect((host, port))
 






















































