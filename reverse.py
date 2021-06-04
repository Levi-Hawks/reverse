#!/bin/usr/python3

senha = "levi_hawks"
flag = [108, 101, 118, 105, 95, 104, 97, 119, 107, 115, 123, 114, 51, 118, 51, 114, 53, 101, 125]

def give_flag(password):
    
  if password == senha:
    print("Senha correta! Sua flag está aqui: ")
    
    for i in range(len(flag)):
      print(chr(flag), end='')
    
  print()

give_flag(input("Qual a senha? "))
