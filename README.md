# API para cadastrar materiais

Este pequeno projeto é um MVP integrante da sprint I (Desenvolvimento Full Stack Básico) da pós-graduação em Engenharia de Software da PUC Rio. 

# Justicativa:

A eficiência e confiabilidade dos sistemas de automação industrial dependem, em grande parte, do pronto acesso a materiais de reposição e manutenção. Para otimizar esse processo crítico, foi desenvolvido uma API para o gerenciamento de materiais em um almoxarifado dedicado à armazenar suprimetos de reposição para manutenção em sistemas de automação industrial. 


# Funcionalidades:

Registro de materiais: a API permitirá o cadastro de materiais de reposição informando sua descrição, quantidade e grupo ao qual o material pertence;

Listar todos os materias disponíveis em estoque;


Melhorar o planejamento da manutenção ao fornecer sobre o estoque disponível.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

Link para o front: 
