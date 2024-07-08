string_name = "this is string it 's"
print(string_name)
print(len(string_name))
a= 'kushal gulo'
for i in a:
 print (i)
email = input('enter your email:')
if '@' not in email :
 print('invalid email')
else:
 print('Email valid sucessfully')

 example = 'favourite food is mango'
 print(example[2:8])

 b='hello world'
 print(b[0:5:2])

 #modifying string
 sentence ='the world is beautiful so lets be happy'
 print(sentence.upper())

 #to remove whitespace
new_sentence='texas college of managment and it'
print(new_sentence.strip())

#to replace anything character add a word from a string we use replace
print(new_sentence.replace('texas','texas college of managment and it'))

#spitting string
split_name= 'Anmol kc'
print(split_name.split('!'))
print(type(split_name.split('!')))

#string concatination
first_Name="gautam shah"
last_Name="shah"
cocncate_Name=first_Name+""+last_Name
print(cocncate_Name)

def sum (a,b):
    sum = a+b
    return sum
sum_amt=sum(20,40)
print(sum_amt)

#sets in python
set_item={'ram','shyam','hari','gopal'}
