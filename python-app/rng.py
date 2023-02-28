"""
# Temporal Method
docker build -t pythontest:latest .
docker run --rm -it pythontest:latest  

# 
docker build -t pythontest:latest
docker run --name pythoncontainer -it pythontest:latest  
docker start -a -i pythoncontainer
"""
from random import randint

min_number = int(input("Please enter the min number: "))
max_number = int(input("Please enter the max number: "))

if (max_number < min_number): 
  print('Max number is less min number. Invalid input...')
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)

