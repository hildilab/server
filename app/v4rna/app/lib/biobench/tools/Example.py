import formencode
from formencode import validators
from formencode import htmlfill

from biobench.tools import BaseController
from biobench.framework import expose


class ExampleValidator(formencode.Schema):
    text = validators.UnicodeString(not_empty=True)
    integer = validators.Int(not_empty=True)
    
class ExampleController( BaseController ):
    def __init__( self, app ):
        """Initialize an interface for the example tool"""
        self.app = app
    @expose
    def index( self, trans, **kwargs ):
        default_values = { 'text': '', 'integer': '3' }
        return self.form( trans, **default_values )
    @expose
    def form( self, trans, **kwargs ):
        input = kwargs
        print input
        try:
            ok = ExampleValidator.to_python(input)
        except validators.Invalid, e:
            print e.value
            return htmlfill.render(trans.fill_template('example.mako'), input, e.error_dict or {})
