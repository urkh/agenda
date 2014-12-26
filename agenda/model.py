
from sqlalchemy.schema import Column
import sqlalchemy.types
from sqlalchemy import Unicode, Date    
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
import camelot.types
    #class movie agragada
#class Movie(Entity):
#
#    __tablename__ = 'movie'
#
#    title = Column(Unicode(60), nullable = False)
#    short_description = Column(Unicode(512))
#    release_date = Column(Date())
#    genre = Column(Unicode(15))
#
#    def __unicode__(self):
#        return self.title or 'Untitled movie'
#
#    class Admin(EntityAdmin):
#        verbose_name = 'Movie'
#        list_display = ['title', 'short_description', 'release_date', 'genre']

class Cliente(Entity):

    __tablename__ = 'cliente'

    Nombre = Column(Unicode(60), nullable = False )
    Cedula = Column(Unicode(9), )
    RIF = Column(Unicode(12),)
    Direccion = Column( Unicode(512) )
    Apartado_Postal = Column (Unicode(6))
    Telefono = Column(Unicode(22))
    Registo_Mercantil = Column(Unicode(14))
    Sitio_Web = Column (Unicode(100))
    Fecha_Creado = Column( Date() )
    Genero = Column(Unicode(15) )

    def __unicode__( self ):
        return self.Nombre or 'NOMBRE NO COLOCADO'
        return self.RIF or 'RIF NO COLOCADO'
    
    class Admin( EntityAdmin ):
        verbose_name = 'Cliente'
        list_display = ['Nombre', 'Cedula', 'RIF', 'Direccion', 'Apartado_Postal', 'Telefono', 'Registro_Mercantil', 'Sitio_Web', 'Fecha_Creado', 'Genero']
