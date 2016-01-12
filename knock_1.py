# -*- coding: utf-8 -*-
import string

# 00.文字列の逆転
# def switch(str):
#     length = len(str)
#     new_str = ""
#     for i in range(length):
#         new_str += str[length - 1 - i]
#     return new_str
#
# print  switch("stressed")
#
string = "stressed"
print string[::-1]


# 01.パタトクカシー
string = u"パタトクカシー"
print string[::2]
# new_str = ""
# for i in range(len(str)/2 + 1):
#     new_str += str[2 * i]
# print new_str


# 02 パトカー + タクシー
pat = u"パトカー"
taxi = u"タクシー"
print(''.join([p + t for (p,t) in zip(pat, taxi)]))


# 03 円周率
string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
num = []

for word in string.split(" "):
    word = word.replace(",", "")
    word = word.replace(".", "")
    num.append(len(word))

print num


# 04 元素記号
string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
elements = {}
for i, word in enumerate(string.replace(",","").replace(".","").split(" ")):
    if i in [1,5,67,8,9,15,16]:
        elements[word[0:2]] = i + 1
    else:
        elements[word[0]] = i + 1

print elements


# 07 テンプレートによる文字生成

def template(x,y,z):
    string = str(x) + "時の" + str(y) + "は" + str(z)
    return string

print template(12, "気温", 22.4)


# 08 暗号文

def cipher(string):
    new_string = ""
    for char in string:
        if char.isalpha() && char.islower():
            new_string += chr(219 - ord(char))
        else:
            new_string += char
