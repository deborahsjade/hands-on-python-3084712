greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print("intrupution", intrupution)
print("formatted", formatted)
print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Tagima"))
print(formatted.lower().capitalize())
