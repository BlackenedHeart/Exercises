def divisibility():
    A = int(input('Enter an integer P: ')) 
    Q = int(input('Enter an integer Q: '))
    if A % Q == 0:
      print(f'{Q} divides {A}')
    else:
      print(f'{Q} does not divides {A}')

divisibility()
