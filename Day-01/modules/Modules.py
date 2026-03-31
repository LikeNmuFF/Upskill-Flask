from package1.module1 import welcome_module1
from package1.module1 import world_module1
from package2.module2 import welcome_module2
from package2.module2 import world_module2
from package3.module3 import welcome_module3
from package3.module3 import world_module3
import module4

print("-" * 50)
#testing for module1
print("Module1 testing")
print(welcome_module1())
print(world_module1())
print("-" * 50)

#tsting for module2
print
print(welcome_module2())
print(world_module2())
print("-" * 50) 

#testing for module3
print("Module3 testing")
print(welcome_module3())
print(world_module3())


#testing for module4
print("-" * 50)
print("Module4 Testing")
print(module4.welcome_module4())
print(module4.world_module4())