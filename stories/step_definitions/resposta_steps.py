# coding: latin-1

from pycukes import *
from should_dsl import *
from zope.testbrowser.browser import Browser
from lxml.html import fromstring
import re


HOME = 'http://localhost:8000/'


@DadoQue('eu colei um "$texto"')
def colar_texto(contexto, texto):
  contexto._pagina = Browser(HOME)
  contexto._pagina.getControl(name='codigo').value = texto
  contexto._pagina.getControl(name='enviar').click()


@Quando('coloco um "$texto"')
def inserir_codigo(contexto, texto):
  contexto._pagina.getControl(name='codigo').value = texto

@Entao('eu vou para outra página')
def verifica_se_esta_em_outra_pagina(contexto):
  contexto._pagina.url |should_not_be.equal_to| HOME

@Quando('eu clico no link "$link"')
def clicar_em_link(contexto, link):
  contexto._pagina.getLink(text=link).click()

@Quando('adiciono um "$texto"')
def adicionar_texto(contexto, texto):
  contexto._pagina.getControl(name='codigo').value += texto
