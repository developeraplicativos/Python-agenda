import os

class Agenda:
    """
    Registo de atividades com opções de
    leitura, edição, exclusão e inserção
    """
    NOME_ARQUIVO = 'agenda_.txt'

    def __init__(self):
        self.menu()

    def clear_screen(self): 
        """
        Limpa a tela do console
        """
        if os.name == 'nt':   
            os.system('cls')
        else:  
            os.system('clear')

    def visualizar(self): 
        self.clear_screen() 
        try: 
            with open(self.NOME_ARQUIVO, 'r') as arquivo: 
                line = arquivo.readlines() 
                for contador, line in enumerate(line):
                    print(f'{contador+1}.  {line}') 
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()
    



    def editar(self): 
        novaAtividade = input('O que você deseja adicionar? ')
        posicao = int(input('Qual a posição q voce deseja substituir? '))

        try: 
            with open(self.NOME_ARQUIVO, 'r') as arquivo:
                atividades = arquivo.readlines() 

                if 1 <= posicao <= len(atividades): 
                    atividades[posicao - 1] = novaAtividade+'\n' 
                    
                    with open(self.NOME_ARQUIVO, 'w') as arquivo:
                        arquivo.writelines(atividades)
                
                else:
                    print('Não existe uma lista pre definida')
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()
         

    def buscar(self):
        termo = input('O que você está procurando? ')
        try: 
            with open( self.NOME_ARQUIVO, 'r') as arquivo:
                atividades = arquivo.readlines()

                if atividades:
                    resultados = [atividade.strip() for atividade in atividades if termo.strip().lower() in atividade.strip().lower()]
                    print('--'*20)
                    if resultados:
                        for i, line in enumerate( resultados):
                            print(f'{i+1}. {line}')
                    else:
                        print('NO RESULTS'.center(40))
                    print('--'*20)
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()

    def excluir(self):
        try: 
            with open(self.NOME_ARQUIVO, 'r') as arquivo:
                atividades = arquivo.readlines()
            
            if atividades:
                indice = int(input('Qual posição quer excluir? '))
                if 1 <= indice <= len(atividades):
                    atividades.pop(indice - 1) 
                    with open(NOME_ARQUIVO, 'w') as arquivo:
                        arquivo.writelines(atividades) 
                else:
                    raise ValueError('Indique uma posição existente')
            else:
                print('Não existe uma lista pre definida')
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()     

    def adicionar(self):
        atividade = input('O que você deseja adicionar? ')
        try: 
            with open(self.NOME_ARQUIVO, 'a') as arquivo:
                arquivo.write(atividade+'\n') 
            
            self.clear_screen()
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex)
        finally:
            if 'arquivo' in locals() and not arquivo.closed: arquivo.close()
    

    def opcoes(self):
        print('-'*40)
        print('OPCOES'.center(40))
        print('-'*40)
        print('1. '.ljust(30)+'visualizar'.rjust(10))
        print('2. '.ljust(30)+'Adicionar'.rjust(10))
        print('3. '.ljust(30)+'Editar'.rjust(10))
        print('4. '.ljust(30)+'Buscar'.rjust(10))
        print('5. '.ljust(30)+'Excluir'.rjust(10)) 
        print('0. '.ljust(30)+'Sair'.rjust(10)) 

    def menu(self):
        while True:
            # clear_screen()
            self.opcoes()
            opcao = input('Qual opção você deseja: ')
            # visualizar
            if opcao == '1':
            # adicionar
                self.visualizar()
            elif opcao == '2':
                self.adicionar()
            # editar
            elif opcao == '3':
                self.editar()  
            # buscar
            elif opcao == '4':
                self.buscar()
            # excluir 
            elif opcao == '5':
                self.excluir()
            elif opcao == '0':
                break
            else:
                print('Opção não encontrada')
 

if __name__ == '__main__':
    agenda = Agenda() 