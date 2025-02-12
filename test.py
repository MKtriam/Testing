age = int(input("Enter your Age:"));

if age<18:
    print("You are a child");
elif age>=18 and age<=30:
    print("You are a teenager");
elif age>30 and age<50:
    print("You are a adult");
else:    
    print("You are a senior");


Temp = int(input("Enter Temperature:"));

if Temp not in range(96,98):
    print("Temperature is not in range");
elif Temp<0:
    print("Temperature is negative");
elif Temp>100:
    print("Temperature is greater than 100");
else:
    print("Temperature is in range");


trying = 0;
while trying<5:
    print("Trying to connect to the internet");
    trying+=1;
    if trying==5:
        print("Failed to connect to the internet");
        break;
    else:
        print("Connected to the internet");
        break;

name = None;

while not name:
    name = input("Enter your name: ");

print("Hello",name);

for i in range(10):
    print(i+1);

for i in "Dev Code":
    print(i);

for i in range(5):
    for j in range(10):
        print("@",end="");
    print();
