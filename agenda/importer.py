from camelot.admin.action import Action
from camelot.core.utils import ugettext_lazy as _

class ImportCovers( Action ):
    verbose_name = _('Import cover images')

    def model_run( self, model_context ):
        from camelot.view.action_steps import ( SelectFile, UpdateProgress, Refresh, FlushSession )
        
        select_image_files = SelectFile( 'Image Files (*.png *.jpg);;All Files (*)' )
        select_image_files.single = False
        file_names = yield select_image_files
        file_count = len( file_names )
