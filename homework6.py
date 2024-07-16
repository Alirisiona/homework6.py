my_dict = {"Alexander":1999, "Maria":2001, "Vera":2003}
print(my_dict)
print(my_dict["Maria"])
print(my_dict.get ("Boris","Такого ключа нет"))
my_dict.update({"Anna":2004,"Sofia":2007})
print(my_dict)
a = my_dict.pop ("Vera")
print (my_dict)
print (a)
print(my_dict)

my_set = {("Apple","Pineapple"), 3, 4, 2, 5, 8, 7, True, 4, 2, 6, 7}
print (my_set)
my_set.add ("Banana")
my_set.add ("Orange")
print (my_set)
my_set.discard (True)
print (my_set)