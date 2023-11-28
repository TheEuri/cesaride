# Contribuições para o Cesaride 🚗
Seja bem-vindo ao nosso projeto! Agradecemos pelo interesse na nossa aplicação. Aqui iremos passar algumas informações para você que deseja contribuir com o CesaRide, por favor, leia-as com atenção!

## Primeiras Etapas
Por favor, verifique se existem issues já registradas relacionadas ao que você deseja fazer. Se encontrar alguma, participe da discussão oferecendo suas sugestões. Se não encontrar nenhuma, sinta-se à vontade para criar uma nova e assim, iniciar uma nova discussão.

Caso deseje, você também pode escolher enviar um pull request diretamente. Lembre-se de certificar-se de descrever detalhadamente todas as suas adições ou criações planejadas.

## Preparando o Ambiente
**PASSO 1:** Certifique-se de possuir o Python instalado em seu sistema, faça o download do Python 3.12.0 em https://www.python.org/

**PASSO 2:** Clone o nosso repositório usando o comando
```
git clone https://github.com/Theeuri/cesaride`
```

**PASSO 3:** Faça a criação do ambiente virtual na sua máquina

```
cd CesaRide
```

```
python -m venv venv
```

**PASSO 4:** Inicie o ambiente virtual de acordo com o sistema operacional de seu uso:
- Windows:
  ```
  venv\scripts\activate
  ```
- MacOS / Linux:
  ```
  source venv/bin/activate
  ```

**PASSO 5:** Instale as dependências necessárias para o serviço
```
pip install -r requirementes.txt
```

**PASSO 6:** Inicie o seu servidor local para a aplicação
```
python manage.py runserver
```
- OBS.: Certifique-se de estar no diretório onde se encontra o arquivo manage.py, caso não esteja utilize o comando cd no terminal para navegar para ele


## Como contribuir com o nosso código:

Primeiramente faça um fork do projeto, após isso crie uma branch com as suas próprias modificações `git checkout -b modificaçõesexemplo`, em seguida faça um commit de suas mudanças utilizando `git commit -m 'Modificações'`. Logo após, você deve fazer um push na sua branch utilizando  `git push origin modificaçõesexemplo`, por fim, faça um pull request com as suas devidas mudanças.
