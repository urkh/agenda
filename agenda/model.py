
from sqlalchemy.schema import Column
import sqlalchemy.types
from sqlalchemy import Unicode, Date    
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
import camelot.types
    #class movie agragada
class Movie(Entity):

    __tablename__ = 'movie'

    title = Column(Unicode(60), nullable = False)
    short_description = Column(Unicode(512))
    release_date = Column(Date())
    genre = Column(Unicode(15))

    def __unicode__(self):
        return self.title or 'Untitled movie'

    class Admin(EntityAdmin):
        verbose_name = 'Movie'
        list_display = ['title', 'short_description', 'release_date', 'genre']


