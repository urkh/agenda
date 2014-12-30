from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import Unicode, Date, Integer
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, relationship
from camelot.admin.action import Action
from camelot.view.action_steps import PrintHtml
from camelot.core.utils import ugettext_lazy as _
from camelot.view.art import Icon


class PrintReport( Action ):      # <------ IMPRIMIR UN REPORTE DE MANERA TOTAL DE CUALQUIER SECCION

    verbose_name = _('Print Report')
    icon = Icon('tango/16x16/actions/document-print.png')
    tooltip = _('Print a report with all the movies')

    def model_run( self, model_context ):
        yield PrintHtml( 'Hello World' )


class Movie(Entity):

    __tablename__ = 'movie'

    title = Column(Unicode(60), nullable=False)
    short_description = Column(Unicode(512))
    release_date = Column(Date())
    genre = Column(Unicode(15))

    director_id = Column(Integer, ForeignKey('director.id'))
    director = relationship('Director', backref='movies')

    def __unicode__(self):
        return self.title or 'Untitled movie'

    class Admin(EntityAdmin):
        verbose_name = 'Movie'
        list_display = ['title', 'short_description', 'release_date', 'genre', 'director']

class Director(Entity):

    __tablename__ = 'director'

    name = Column(Unicode(60))

    class Admin(EntityAdmin):
        verbose_name = 'Director'
        list_display = ['name']
        form_display = list_display + ['movies']

    def __unicode__(self):
        return self.name or 'unknow director'


class Cliente(Entity):

    __tablename__ = 'cliente'

    nombre = Column(Unicode(60), nullable = False )
    cedula = Column(Unicode(9), )
    rif = Column(Unicode(12),)
    direccion = Column( Unicode(512) )
    apartado_postal = Column (Unicode(6))
    telefono = Column(Unicode(22))
    registro_mercantil = Column(Unicode(14))
    sitio_web = Column (Unicode(100))
    fecha_creado = Column( Date() )
    genero = Column(Unicode(15) )

    def __unicode__( self ):
        return self.nombre or 'Sin nombre'
    
    class Admin( EntityAdmin ):
        verbose_name = 'Cliente'
        list_display = ['nombre', 'cedula', 'rif', 'direccion', 'apartado_postal', 'telefono', 'registro_mercantil', 'sitio_web', 'fecha_creado', 'genero']

