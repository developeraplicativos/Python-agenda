class Archives: 

    def __init__(self):
        self.__NOME_ARQUIVO = 'arq/agenda_.txt' 

    def read_archive(self):
        try: 
            with open(self.__NOME_ARQUIVO, 'r') as arquivo:  
                return arquivo.readlines() 
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex) 

    def read_lines_full(self):
        try:  
            with open(self.__NOME_ARQUIVO, 'r') as arquivo:  
                for index, line in enumerate(arquivo): 
                    yield {'ordem':index,'nome':f"{line.rstrip('\n')}"}
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(f"Ocorreu um erro: {ex}")  

    def write_lines_archive(self, conent):
        try: 
            with open(self.__NOME_ARQUIVO, 'w') as arquivo:
                arquivo.writelines(conent)
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()

    def write_archive(self, conent):
        try: 
            with open(self.__NOME_ARQUIVO, 'a') as arquivo:
                arquivo.write(conent)
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()

    def edit_archive(self, content):
        try:
            with open(self.__NOME_ARQUIVO, 'w') as arquivo:
                arquivo.writelines(content)

        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()