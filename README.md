# dashboard-tccs-ufrn
Dashboard interativo para análise de dados de Trabalhos de Conclusão de Curso da UFRN


## Desenvolvimento

```sh
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências
python -m pip install -r requirements.txt

# Execute a aplicação
python -m gunicorn --reload --chdir app dashboard:server
```

## Autores

[@neumanf](https://www.github.com/neumanf) e [@jamlemoos](https://www.github.com/jamlemoos) 

## Licença

MIT

