from collections import OrderedDict #take "OrderedDict" datatype from Package "collections", though after python 3.7 onwards dictionaries are byDefault OrderedDict i.e. they maintain the order of the elements in which they were added to the list i.e. we don't need to import anything, if we are working with Python 3.7 or above.

groceries = {'bananas':5, "oranges":3}
print(groceries.get("hello"))
print(groceries.get("bananas"))

groceries.__setitem__('bananas',2)
print(groceries.get("bananas"))


#Dictionary inside a Dictionary
contacts = {
  'Joe': {
    'phone': '1213132', 'email':'afff@g.com'
    },
  'jane':{
    'phone': '1213132', 'email':'afff@g.com'
  }
}
print(contacts.get('jane'))
print(contacts.get('jane').get('email'))

#Extra:
sentence = "I like the name Sidharth bcoz the name Sidharth is the best"

word_list = sentence.split(" ")
print(word_list)
print()

word_count = {word_list[0]:0}
print("Starting Dictionary: " + str(word_count))
print()

#Add all the words in word_list and count them
for i in range(len(word_list)):
  
  count_of_a_word = word_count.get(word_list[i])
  
  if(word_count.get(word_list[i])==None):
    word_count.update({word_list[i]:1})
  else:
    word_count.update({word_list[i]:count_of_a_word+1})

print("Updated Dictionary: " + str(word_count))
print()

# if u want to initiate an empty dictionary: 
w = dict.fromkeys([])
print("current dict w: " + str(w))
w.update({"sda":2, "sadf": 4})
print("after update, dict w: " + str(w))
print()

#list the items:
print("items of dictionary: ")
print(w.items())
print(list(w.items()))
print()

#list the keys:
print("keys of dictionary: ")
print(w.keys())
print(list(w.keys()))
print()

#list the values:
print("values of dictionary: ")
print(w.values())
print(list(w.values()))
print()

#pop the particular item
print("popped: "+str(w.pop("sda")))
print("after poping particular item: "+str(w))
print()

#pop the upper most item
print("popped: "+str(w.popitem()))
print("after poping the upper most item: "+str(w))
print()

print(w.clear())