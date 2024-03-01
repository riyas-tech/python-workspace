words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print ("Words        :", words)
print ("Sorted Words :", sorted_words)


products = [{"name" : "A", "price" : 50}, {"name" : "B", "price" : 30}]
filtered_products = filter(lambda x : x['price'] > 40, products)
print("Products           :", products)
for item in filtered_products:
    print(item)