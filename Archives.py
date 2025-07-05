class Archives:
    __NOME_ARQUIVO = 'agenda_.txt'

    def __init__(self):
        self.__NOME_ARQUIVO = 'agenda_.txt'

    def readArchive(self):
        try: 
            with open(self.__NOME_ARQUIVO, 'r') as arquivo:  
                return arquivo.readlines() 
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex) 

    def writeLinesArchive(self, conent):
        try: 
            with open(self.__NOME_ARQUIVO, 'w') as arquivo:
                arquivo.writelines(conent)
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()

    def writeArchive(self, conent):
        try: 
            with open(self.__NOME_ARQUIVO, 'a') as arquivo:
                arquivo.write(conent)
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()