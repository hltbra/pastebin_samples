from juno import *
from models import (Codigo,
                    db_session,
                    setup_all,
                    metadata)


init({'template_root': '../templates/',
      'static_root': '../static/'})


@get('/')
def index(web):
    id_codigo_origem = web.input('codigo_origem')
    tipo_do_codigo = web.input('tipo')
    codigo = Codigo.get_by(id=id_codigo_origem)
    if codigo is None:
        return template('index.html')
    return template('index.html',
                    texto=codigo.texto)

@post('/paste')
def colar_codigo(web):
    novo_codigo = Codigo(texto=web.input('codigo'),
                         tipo=web.input('tipo'))
    db_session.commit()
    redirect('/%d' % novo_codigo.id)


@get('/:id')
def mostrar_codigo_versionado(web, id):
    return template('mostrar_codigo.html',
                    codigo=Codigo.get_by(id=id),)


if __name__ == '__main__':
#    import os
#    diretorio = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    metadata.bind = 'sqlite://'#/' + os.path.join(diretorio, 'test.db')
    setup_all(True)
    run()
