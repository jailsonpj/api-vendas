# API Vendas

API RestFul para disponibilização de dados de vendas de produtos.

# Módulos API
A API consome dados que estão armazenados no Elasticsearch Clound, uma ferramenta de busca indexada. Os dados foram coletados e processados, antes de serem armazenados no elasticsearch.

- **elastic.py** : script de serviço que faz a conexão com a clound do elasticsearch e disponibiliza um client para o consumo de dados armazendados na clound.
- **main.py**: script responsável pela criação da API restful, elas faz utlização do FastAPI (uma biblioteca python para criação de api rest). A partir desse arquivo que as visões e informações serão disponíveis pela API.

# Arquivos de configuração
 - **Procfile** : O procfile é um arquivo de configuração responsável pela execução da API no Heroku.
 - **requirements.txt**: arquivo txt contendo as dependencias que são utilizadas na build da API.