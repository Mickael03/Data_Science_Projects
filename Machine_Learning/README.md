Contém os códigos do livro:

>[Machine Learning – Guia de Referência Rápida](https://novatec.com.br/livros/machine-learning-guia-referencia/)

Editora: Novatec, São Paulo.  
Escrito: Matt Harrison

# Guia Rápido de Configuração de Ambiente

Este guia contém os comandos essenciais para configurar o ambiente Python. Usaremos o `pyenv` para gerenciar as versões do Python e o `venv` para criar ambientes virtuais isolados.

## [Pyenv](https://github.com/pyenv/pyenv)

Ferramenta para controle de múltiplas versos do python.  

[![pyenv](https://avatars.githubusercontent.com/u/46895318?s=200&v=4)](https://github.com/pyenv-win/pyenv-win)  

Guia de instalação: [Pyenv for Windows](https://github.com/pyenv-win/pyenv-win)  

> Instalação de uma versão:   
`pyenv install <versao>`

> Versão do pyenv   
`pyenv --version`

> Mostrar versão local  
`pyenv local --version`

> Mostrar versão global     
`pyenv global --version`

> Mostrar versões disponíveis   
`pyenv versions`

## [Venv](https://docs.python.org/3/library/venv.html) 

Módulo para criar ambientes virtuais

> criar um ambiente:  
`python -m venv meu_ambiente`  

> Ativa o ambiente:  
``meu_ambiente\Scripts\activate`` (Windows)    
``source meu_ambiente/bin/activate`` (Linux/macOS)  

> Instação dos pacotes:  
``pip install pacotes``  

> Criar arquivo com versões de pacotes  
`pip freeze > requirements.txt`  

> Instalações de pacotes a partir de uma arquivo  
`pip install -r requirements.txt`  

> Desativa o ambiente:  
`deactivate`