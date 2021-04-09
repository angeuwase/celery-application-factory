from . import main_blueprint
from ..email import reverse_name

@main_blueprint.route('/home/<name>',)
def index(name):
    #result = reverse_name.apply_async(args=[name], queue='Calc')
    result = reverse_name.apply_async(args=[name])

    return name