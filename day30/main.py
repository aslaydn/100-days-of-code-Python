######################## ERRORS ############################

'''
try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["kgjlfhjl"]) #key error
except FileNotFoundError:
    # trydaki satirlar hata verirse except calisir.
    file = open("a_file.txt","w")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")    
else: #hata yoksa kosar
    content = file.read()
    print(content)
finally: #ne olursa olsun calisir.
    file.close()
'''

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

