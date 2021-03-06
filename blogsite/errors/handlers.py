from flask import Blueprint, render_template, url_for

errors = Blueprint('errors', __name__)

#You can return two values when the second is an error code, default is 200 but we want to return error codes.
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
