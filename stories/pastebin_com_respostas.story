História: Aceitando respostas aos pastes
  Para que o meu pastebin seja mais colaborativo
  Como um cara interessado em saber a opinião dos outros
  Eu quero que as pessoas possam responder os pastes

  Cenário: Mudando de página na resposta
    Dado que eu colei um "echo hello world"
    Quando eu clico no link "responder"
    Então eu vou para outra página

  Cenário: Criando uma resposta
    Dado que eu colei um "echo hello world"
    Quando eu clico no link "responder"
    E adiciono um "print 'hello world'"
    E eu clico em "enviar"
    Então eu vejo "echo hello world" 
    E eu vejo "print 'hello world'"
    E eu vejo "novo paste"
