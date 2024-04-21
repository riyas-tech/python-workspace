state_names = ["Arizona", "California", "California", "Kentucky", "Louisiana"]
county_names = ["Maricopa", "Alameda", "Sacramento", "Jefferson", "East Baton Rouge"]


state_county_tuples = []
for i in range(len(state_names)):
    state_county_tuples.append((state_names[i], county_names[i]))

print(state_county_tuples)

a = ['a', 'b', 'c']
b = [1,2,3]

c = zip (a, b)

print(list(c))

state_country_zipped = list(zip(state_names, county_names))
print(state_country_zipped)