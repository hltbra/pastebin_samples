from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from elixir import *


class Codigo(Entity):
    texto = Field(UnicodeText)
    tipo = Field(String(10), required=True, default='text')

    def converter_pra_html(self):
        lexer = get_lexer_by_name(self.tipo)
        return highlight(self.texto, lexer, HtmlFormatter())


db_session = session
