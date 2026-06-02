print("Bem vindo ao Dicionário de status HTTP")
codigo = int(input("Digite o codigo do status HTTP e pressione ENTER: "))
match codigo:
    case 200:
        print("CÓDIGO 200- É a resposta padrão que indica sucesso em uma requisição web.")
    case 400:
        print("CÓDIGO 400- Bad Request: A solicitação não pode ser processada devido a erro de sintaxe.")
    case 401:
        print("CÓDIGO 401- Unauthorized: Acesso negado; requer autenticação válida.")
    case 403:
        print("CÓDIGO 403- Forbidden: O servidor entende a requisição, mas se nega a autorizá-la.")
    case 404:
        print("CÓDIGO 404- Not Found: O servidor não encontrou o recurso/página solicitado.")
    case 500:
        print("CÓDIGO 500- Internal Server Error: Erro genérico no servidor que impede a conclusão da requisição.")
    case _:
        print("Digite um código Cadastrado!")