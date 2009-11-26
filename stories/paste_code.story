História: Colando Código
  Para que eu tenha um pastebin
  Como um programador
  Eu quero deixar as pessoas verem meus códigos

  Cenário: Colando código
    Dado que eu estou na página inicial do pastebin
    E eu não tenho nenhum código salvo
    Quando eu digito um simples "hello world"
    E eu clico em "enviar"
    Então eu vejo o meu "hello world" colado
    E vejo que a url possui o id 1
  
  Cenário: Colando outro código
    Dado que eu estou na página inicial do pastebin
    Quando eu digito um simples "hello world2"
    E eu seleciono o tipo "Python"
    E eu clico em "enviar"
    Então eu vejo o meu "hello world2" colado como código python
    E vejo que a url possui o id 2
     
  Cenário: Acessando o primeiro código
    Dado que eu vou para a página do código de id 1
    Então eu vejo "hello world"
     
