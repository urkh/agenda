from camelot_example.importer import ImportCovers
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _


class MyApplicationAdmin(ApplicationAdmin):

    name = 'Agenda de Contactos'
    application_url = 'http://github.com/urkh/agenda'
    help_url = 'http://github.com/urkh/agenda'
    author = 'Gustavo Leon y Marcos Castellanos'
    domain = 'http://github.com/urkh/agenda'

    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        from model import Movie, Director, Cliente
        return [
            Section(
                _('Contactos'),
                self,
                Icon('tango/22x22/apps/system-users.png'),
                items=[Cliente]
            ),
            Section( _('Movies'),
                         self,
                         Icon('tango/22x22/mimetypes/x-office-presentation.png'),
                         items = [ Movie, Director, 
#                                   VisitorsPerDirector,
                                   ImportCovers() ]),
            Section(
                _('Configuracion'),
                self,
                Icon('tango/22x22/categories/preferences-system.png'),
                items=[Memento, Translation]
            )
        ]
