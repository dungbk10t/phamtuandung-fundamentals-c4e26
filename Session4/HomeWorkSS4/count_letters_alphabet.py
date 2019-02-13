#Bài 20.8.1 T273 sách thinkcspy3
string = "ThiS is String with Upper and lower case Letters"
string_after1 = string.lower() #Chuyển ký tự hoa thành thường
string_after2 = string_after1.replace(' ', '') #loại bỏ dấu cách
string_after3 = sorted(string_after2) #sắp xếp các ký tự theo alphabet
# print(string_after3)
letter_counts = {}
for letter in string_after3:
    letter_counts[letter] = letter_counts.get(letter,0) + 1

for (key,value) in letter_counts.items():
    print(key,value," ")