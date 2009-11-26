from web.contrib.template import render_jinja
from models import (Codigo,
                    db_session,
                    setup_all,
                    metadata)
import web


metadata.bind = 'sqlite://'
setup_all(True)

urls = ('/', 'index',
        '/paste', 'paste',
        '/(\d+)', 'mostrar')

render = render_jinja('../templates')


class index:
    def GET(self):
        valores = web.input(codigo_origem=None)
        id_codigo_origem = valores['codigo_origem']
        if id_codigo_origem:
            return render.index(texto=Codigo.get_by(id=id_codigo_origem).texto)
        return render.index()


class paste:
    def POST(self):
        form = web.input(codigo={}, tipo={})
        novo_codigo = Codigo(texto=form['codigo'],
                             tipo=form['tipo'])
        db_session.commit()
        raise web.seeother('/%d' % novo_codigo.id)

class mostrar:
    def GET(self, id):
        return render.mostrar_codigo(codigo=Codigo.get_by(id=id))

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
