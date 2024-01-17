#7장 튜플과 리스트 연습문제
#7.1
'''
year_lists=[2001,2002,2003,2004,2005,2006]
'''

#7.2
'''
year_lists=[2001,2002,2003,2004,2005,2006]
print(year_lists[2])
'''

#7.3
'''
year_lists=[2001,2002,2003,2004,2005,2006]
print(year_lists[5])
'''

#7.4
'''
things = ["mozzarella","cinderella","salmonella"]
'''

#7.5
#대문자로 바꾸는 방법 1) 첫 글자만 바꾸는 함수 capitalize,  2) 전체를 대문자로 바꾸는 함수 upper
'''
things = ["mozzarella","cinderella","salmonella"]
print(things[1].capitalize())
print(things) #['mozzarella', 'cinderella', 'salmonella']
'''
#This way cannot change list's components

#꺼내고 나서 바꾸는 방법
'''
person = things.pop(1)
#print(person) #cinderella
#print(type(person)) #<class 'str'>
person = person.capitalize()
print(person)#CINDERELLA
'''

#7.6
#대문자로 바꾸는 방법 1) 첫 글자만 바꾸는 함수 capitalize,  2) 전체를 대문자로 바꾸는 함수 upper
'''
things = ["mozzarella","cinderella","salmonella"]
print(things[0].upper())
'''

#7.7
'''
things = ["mozzarella","cinderella","salmonella"]
things.pop(2)
print(things)
'''
#7.8
'''
surprise = ["Groucho","Chico","Harpo"]
'''

#7.9
'''
#모두 소문자로 변경하는 법 lower 함수
surprise = ["Groucho","Chico","Harpo"]
a=surprise[2].lower()
#print(type(a)) #<class 'str'>
#print(a) #harpo
#AttributeError: 'str' object has no attribute 'reverse'
#문자열에는 reverse 적용 불가능하니까 문자열 슬라이싱 이용
a=a[-1::-1] #스텝을 음수로 지정
#print(a) #oprah
a=a.capitalize()
#print(a) #Oprah
'''

#7.10
#list comprehension
#[표현식 for 항목 in 순회가능한객체]
#cf.
#even_sqares = [i*i for i in range(1, 5+1, 1) if i % 2 == 0] #짝수의 제곱만 출력 됨
#print(even_sqares)
'''
even_number_list = [i for i in range(10) if (i%2==0 and i!=0)] #0은 출력되면 안되니까 조건 두개 추가
print(even_number_list) #[2, 4, 6, 8]
'''

#7.11
'''
start1=["fee","fie","foe"]
rhymes = [
    ("flop","get a mop"),
    ("fope","turn the rope"),
    ("fa","get your ma"),
    ("fudge","call the judge"),
    ("fat","pet the cat"),
    ("fog","walk the dog"),
    ("fun","say we're done"),
]
start2= "Someone better"

for i in range(2+1):
    print(f"{start1[i].capitalize()}!",end=" ")
print(f"{rhymes[0][0].capitalize()}!")
print(start2,end=" ")
print("%s"%rhymes[0][1])
'''
