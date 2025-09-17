student_name = "Collin"
student_age = 34
product_price = 19.99

# oplossing 1, gebruik van functie str(), dit gaat de variable naar type string omvormen
print(student_name + " is " + str(student_age) + " years old. The product price is " + str(product_price))

# oplossing 2, gebruik van , ipv concat
print(student_name, "is", student_age, "years old. The product price is", product_price)

# oplossing 3 gebruik van f voor de double quotes zorgt ervoor dat ik met {} variabelen kan oproepen
print(f"{student_name} is {student_age} years old. The product price is {product_price}")