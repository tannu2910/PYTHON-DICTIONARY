# # que.1

# Dict={'ball':'green','Ball':'red'}
# print(Dict['ball'])
# print(Dict['Ball'])


# que.2

# student=dict(name="Ravina",age=20)
# print(student)

# que.3

# my_dict={1:'apple',2:'ball'}
# print(my_dict)


# que.4

# my_dict={'name':'john',1:[2,4,3]}
# print(my_dict)


# que.5


# dic={1:'navgukul',2:'in',3:{'A':'welcome','B':'to','c':'dharamsala'}}
# print(a)


# # que.6

# person={'name':'jack','age':20,'gender':'male',4:'organisation'}
# result=person['age']
# x=person.get("gender")
# print(person[4])
# print(x)
# print(result)



# que.7

# person={'name':'jack','age':20,'gender':'male',4:{'organisation':'navgurukul','place':'dharamsala'}}
# print(person['gender'])
# print(person[4])
# result=person[4]['place']
# print(result)


# que.8

# dic={'Name':'Ram','Age':17}
# dic['Organization']="navgurukul"
# dic['place']='dharmsala'
# print(dic)


# que.9

# dic={'Name':'Ram','Age':17,}
# dic['student']={'id':22,'place':'dharmsala'}
# print(dic)


# que.10

# car={'brand':'ford','model':'mustang','year':1964}
# if "model" in car:
#     print("yes,'modal'is one of the keys in the car dictionary.")
# else:
#     print("No,'model'key dictionary me nhi h")


# # updating dictionary//

# # que.1

# person={'1':'Ram','2':17,}
# person[3]='male'
# print(person)


# # que.2

# details={'Name':'Ram','Age':17,'student':{'id':22,'place':'dharmsala'}}
# details['student']['id']=35
# print(details)


# # copy of dictionary///

# # que.1

# classes={"room1":"6th","room2":"7th","room3":"8th"}
# mydict=classes.copy()
# print(mydict)


# #removing element from a dictinary///

# # pop() que..1

# car_details={"brand":"ford",",model":"jason","year":1964}
# car_details.pop("model")
# print(car_details)


# popitem() que..1

# person={'name':'jack','id':22,'place':'dharamsala'}
# person.popitem()
# print(person)


# # del() que..1

# person={'name':'jack','id':22,'place':'dharamsala'}
# del person('place')
# print(person)


# iterate through all keys que..1

# states_capitals={}