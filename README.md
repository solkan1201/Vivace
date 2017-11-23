# Vivace
Este é o código para a plataforma de telemetria desenvolvida pela equipe Céu Azul Aeronaves a partir do ano de 2016

## Documentaçao

A documentaçao da plataforma Vivace, incluindo as *docstrings* de todas as classes e metodos esta disponivel em http://vivace.readthedocs.io .

## Instalar dependencias

Para instalar as dependencias Python basta abrir um terminal na raiz do projeto e usar o comando ```make init```.

Caso voce prefira fazer isso manualmente, todas as dependencias Python necessarias estao listadas no arquivo *requirements.txt*.

## Atualizar documentaçao

1. Realize as mudanças desejadas na documentaçao.
2. Entre na pasta docs e use os comandos:
```
make clean-docs
make docs
make html
```

## Versionamento
Este repositorio utiliza as regras de versionamento semantico descritas no seguinte documento: http://semver.org/lang/pt-BR
