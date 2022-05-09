from flask import render_template, request, Blueprint
from blogsite.models import Post

#Using flask blueprints, like creating an instance of a flask object in __init__, 
#but also passing in the name of the Blueprint in addtiion to __name__
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=7)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')