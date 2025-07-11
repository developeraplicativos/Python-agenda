import re

class User:
    """
    class to login
    verify structure of mail
    verify user
    """
    def __init__(self,email,senha):
        self.__email = email
        self.__senha = senha

    def getEmail(self):
        return self.__email

    def getSenha(self): 
        return self.__senha 

    def setEmail(self, email):
        try:
            if email is not None:
                self.__email = email
            else:
                raise ValueError('O e-mail não pode estar vazio')
        except ValueError as error:
            print(error)
        except Exception as ex:
            print(ex)

 
    def setSenha(self, senha):
        try:
            if senha is not None:
                self.__senha = senha
            else:
                raise ValueError('A senha não pode estar vazia')
        except ValueError as error:
            print(error)
        except Exception as ex:
            print(ex)


    def validaEmail(self): 
        try:
            return bool(re.match(r"^[\w\.-]+\@[\w\.-]+\.[\w]{2,4}$",self.__email)) 
        except Exception as ex:
            print(ex)

    def login(self):
        email = 'emerson@gmail.com'
        senha = '12345' 
        return (self.validaEmail() and email == self.__email and senha == self.__senha)
 