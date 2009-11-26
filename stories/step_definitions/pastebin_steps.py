# coding: latin-1
from pycukes import *
from should_dsl import *
from zope.testbrowser.browser import Browser
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_lexer_by_name

HOME = 'http://localhost:8000'

@DadoQue('eu estou na página inicial do pastebin')
def vai_pra_pagina_inicial(contexto):
  contexto._pagina = Browser(HOME)

@DadoQue('eu não tenho nenhum código salvo')
def apagar_todos_codigos(contexto):
  pass
#  import sqlite3
#  connection = sqlite3.connect('test.db')
#  cursor = connection.cursor()
#  cursor.execute('
#  try:
#    f = open('test.db', 'wb')
#  finally:
#    f.close()
  
@Quando('eu digito um simples "$texto"')
def entrar_com_texto(contexto, texto):
  contexto._pagina.getControl(name='codigo').value = texto

@Quando('eu clico em "$botao"')
def enviar(contexto, botao):
  contexto._pagina.getControl(name=botao).click()

@Entao('eu vejo o meu "$texto" colado')
def vejo_o_texto_colado(contexto, texto):
  contexto._pagina.contents |should_have| texto

@Entao('vejo que a url possui o id $id')
def url_possui_id(contexto, id):
  contexto._pagina.url |should_be.ended_with| ':8000/' + id


@DadoQue('eu vou para a página do código de id $id')
def vai_pra_pagina_de_id(contexto, id):
  contexto._pagina.open(HOME + '/' + id)

@Entao('eu vejo "$texto"')
def procurar_por_texto(contexto, texto):
  contexto._pagina.contents.replace('&#39;', "'") |should_have| texto

@Entao('eu vejo o meu "$texto" colado como código python')
def ver_codigo_python(contexto, texto):
  lexer = get_lexer_by_name('python')
  contexto._pagina.contents |should_have| highlight(texto, lexer, HtmlFormatter())

@Quando('eu seleciono o tipo "$tipo"')
def selecionar_tipo(contexto, tipo):
  campo_tipo = contexto._pagina.getControl(name='tipo')
  options = dict(zip(campo_tipo.displayOptions, campo_tipo.options))
  valor_do_tipo = options[tipo]
  campo_tipo.value = [valor_do_tipo]
