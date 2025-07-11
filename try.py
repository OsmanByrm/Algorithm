
fridge_contents = {"egg":12, "milk": 2, "apple": 6, "celery": 5}
for variable1, variable2 in fridge_contents.items():
    if variable1 in fridge_contents:
        print(fridge_contents[variable1])
    if variable2 in fridge_contents:
        print(fridge_contents[variable2])