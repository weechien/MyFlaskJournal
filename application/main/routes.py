from flask import render_template, request, Blueprint
from application.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', title='Home', posts=posts)
