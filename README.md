# CP02_IA_EQUIPE101_prompt-toolkit

## Estruturas de pastas

```

└── 📁Prompt-Toolkit/

    └── 📁data/ # pasta para armazenamento de dados em formato json

        ├── examples.json # exemplos de respostas para o few shot

        ├── inputs.json # exemplos de inputs

    └── 📁output/ # pasta para armazenamento dos relatorios gerados

        └── 📁graficos/ # pasta para os gráficos gerados por report.py

            ├── acuracia.png # gráfico comparativo da acuracia de cada técnica

            ├── custo.png # gráfico comparativo de custo de cada tecnica
            
            ├── temperatura.png # grafico comparativo entre os resultados da melhor técnica variando temperatura

        ├── resultados.csv # tabelca csv dos resultados

    └── 📁prompts/ # pasta para armazenamento 

        ├── system_prompts.json #
 
        ├── templates.json #

    └── 📁src/ # pasta principal do código do projeto

        └── 📁__pycache__/ # pasta de cache do python

        ├── init.py

        ├── evaluator.py # funções para calculos referentes as respostas 

        ├── llm_client.py # classe para controla da ia
  
        ├── prompt_builder.py # funções geradoras de prompt

        ├── report.py # funções para analise de resultados

        ├── tasks.py # definição das tarefas 

        ├── techniques.py # funções para criação de prompt especializado para cada tecnica

    └── 📁docs/ 

        ├── CP02_101.pdf # documentação do projeto 

    ├── .env.example # variaveis de ambiente

    ├── LICENSE

    ├── main.py # arquivo principal

    ├── README.md 

    └── requirements.txt # arquivo de especificação de dependencias python

```


 

## instalação de dependências


### ollama


para instalação, primeiro é necessário ter o ollama em sua maquina, siga as instruções do [site oficial](https://ollama.com/download), ou copie esses comandos em sua respectiva maquina:


#### Windows


```bash

irm https://ollama.com/install.ps1 | iex

```
 

#### Linux


```bash

curl -fsSL https://ollama.com/install.sh | sh

```


#### MacOS
 

```base

curl -fsSL https://ollama.com/install.sh | sh

```

### Execusão do modelo
 
após ter o ollama em sua maquina, rode com o modelo preferido


```base

ollama run gpt-oss:120b

```

## baixando projeto

com as dependências instaladas, clone o repositorio do projeto em seu computador e depois entre na pasta


```base

git clone https://github.com/gab-dpaula/CP02_IA_EQUIPE101_prompt-toolkit.git


cd CP02_IA_EQUIPE101_prompt-toolkit

```

## Configuração

caso seja necessário mudar o endereço do localhost ou o modelo utilizado, personalize o arquivo .env.example e coloque os valores desejados

```env
OLLAMA_HOST=http://localhost:11434
MODEL=gpt-oss:120b
```

## Excusão

dentro do diretório do projeto rode o arquivo main.py


```bash

python main.py

``` 
