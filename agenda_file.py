import os
from Archives import Archives
from User import User

class Agenda:
    """
    Registo de atividades com opções de
    leitura, edição, exclusão e inserção
    """  

    def __init__(self):

        result = False
        user = User(None, None)
        while result != True:
            user.setEmail(input('Digite seu E-mail: '))
            user.setSenha(input('Digete a senha: '))
            result = user.login()

        if user.login():
            self.menu()
            locals()
        
    @property
    def clear_screen(self): 
        """
        Limpa a tela do console
        """
        if os.name == 'nt':   
            os.system('cls')
        else:  
            os.system('clear')
    
    def visualizar(self): 
        self.clear_screen 
        try: 
            arq = Archives()
            lines = arq.read_archive() 
            for contador, line in enumerate(lines):
                print(f'{contador+1}.  {line}') 
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex) 
    



    def editar(self): 
        novaAtividade = input('O que você deseja editar? ')
        posicao = int(input('Qual a posição q voce deseja substituir? '))

        try: 
            arq = Archives() 
            atividades = arq.read_archive()  
            if 1 <= posicao <= len(atividades): 
                atividades[posicao - 1] = novaAtividade+'\n' 
                arq.edit_archive(atividades)
            
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
            arq = Archives() 
            atividades = arq.read_archive() 
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

    def excluir(self):
        try: 
            arq = Archives()  
            atividades = arq.read_archive()
            
            if atividades:
                indice = int(input('Qual posição quer excluir? '))
                if 1 <= indice <= len(atividades):
                    atividades.pop(indice - 1)  
                    # print(atividades)
                    arq.write_lines_archive(atividades)
                else:
                    raise ValueError('Indique uma posição existente')
            else:
                print('Não existe uma lista pre definida')
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex) 

    def adicionar(self):
        atividade = input('O que você deseja adicionar? ')
        try: 
            archive = Archives()  
            archive.write_archive(atividade+'\n') 
            
            self.clear_screen
        except FileNotFoundError:
            print('O Arquivo ainda não existe, você precisa cadastrar algo')
        except Exception as ex:
            print(ex) 
    

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
 
 
agenda = Agenda() 