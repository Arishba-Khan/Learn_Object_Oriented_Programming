# **Parameter VS Attributes VS Arguments.**


```
class Student:
    def __init__(self, name, age):  # ← parameters
        self.name = name            # ← attributes
        self.age = age              # ← attributes

# create object with arguments
s1 = Student("Arishba", 18)         # ← arguments
print(s1.name)
```

| Term      | What It Is                              | Where It Appears                  | Example Value   |
| --------- | --------------------------------------- | --------------------------------- | --------------- |
| Attribute | Data stored inside an object            | Inside a class (`self.name`)      | `self.name`     |
| Parameter | Placeholder variable in method/function | Inside function/method definition | `name, age`     |
| Argument  | Actual value passed to function         | When calling function             | `"Arishba", 18` |
