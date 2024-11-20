'''
Try Except Exception Handling In Python
'''
print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
try:

    print("The sum of these two numbers is ",
          int(num1)+int(num2))
except Exception as e:                       # Here we catch the error and it print the error line and programm excutes the forward operation.
    print(e)

print("This line is very important")
# Programm error show na kare isliye hum log "Try  except Exception Handling" use karte hai