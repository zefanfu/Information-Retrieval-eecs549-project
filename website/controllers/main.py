from flask import *

from extensions import *

from config import *

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=['GET', 'POST'])
def main_route():

    options = {
      'host': config.env['host'],
      'port': config.env['port']
    }
    return render_template("index.html", **options)
