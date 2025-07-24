import requests

res = requests.post('http://127.0.0.1:5000/acesso')  
if(res.status_code == 200): 
    if(res.json()['access'] == True): 
        print('Sucesso - /acesso') 
    elif(res.json()['error'] == True):
        print(res.json()['msg']) 
else:
    print('Error conexão /acesso')

res = requests.get('http://127.0.0.1:5000/visualizar')
if(res.status_code == 200): 
    if(res.json()['visualizar'] is not None): 
        print(res.json()['visualizar']) 
    elif(res.json()['error'] == True):
        print(res.json()['msg'])
else:
    print('Error conexão /visualizar')

res = requests.post('http://127.0.0.1:5000/editar')
if(res.status_code == 200): 
    if(res.json()['update'] == True): 
        print('Sucesso - /editar') 
    elif(res.json()['error'] == True):
        print(res.json()['msg'])
else:
    print('Error conexão /editar')
 
res = requests.post('http://127.0.0.1:5000/buscar')
if(res.status_code == 200): 
    if(res.json()['search'] is not None): 
        print(f'sucesso - /buscar {res.json()['search']}') 
    elif(res.json()['error'] == True):
        print(res.json()['msg'])
else:
    print('Error conexão /buscar') 

res = requests.post('http://127.0.0.1:5000/excluir')
if(res.status_code == 200): 
    if(res.json()['delete'] == True): 
        print('sucesso - /excluir') 
    elif(res.json()['error'] == True):
        print(res.json()['msg'])
else:
    print('Error conexão /excluir')

res = requests.post('http://127.0.0.1:5000/adicionar')
if(res.status_code == 200): 
    if(res.json()['add'] == True): 
        print('sucesso - /adicionar') 
    elif(res.json()['error'] == True):
        print(res.json()['msg'])
else:
    print('Error conexão /adicionar')