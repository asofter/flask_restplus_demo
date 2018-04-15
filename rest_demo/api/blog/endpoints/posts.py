import logging

from flask import request
from flask_restplus import Resource
from rest_demo.api.blog.business import create_blog_post, update_post, delete_post
from rest_demo.api.blog.serializers import blog_post, page_of_blog_posts
from rest_demo.api.blog.parsers import pagination_arguments
from rest_demo.api.restplus import api
from rest_demo.database.models import Post

log = logging.getLogger(__name__)

ns = api.namespace('blog_posts', path='/blog/posts', description='Operations related to blog posts')


@ns.route('/')
class PostsCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_blog_posts)
    def get(self):
        """
        Returns list of blog posts.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        posts_query = Post.query
        posts_page = posts_query.paginate(page, per_page, error_out=False)

        return posts_page

    @api.expect(blog_post)
    def post(self):
        """
        Creates a new blog post.
        """
        create_blog_post(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class PostItem(Resource):

    def get_by_id(self, id):
        post = Post.query.get(id)
        if post:
            return post
        else:
            return api.abort(404, "Post not found.")

    @api.marshal_with(blog_post)
    def get(self, id):
        """
        Returns a blog post.
        """
        post = self.get_by_id(id)
        return post

    @api.expect(blog_post)
    @api.response(204, 'Post successfully updated.')
    def put(self, id):
        post = self.get_by_id(id)

        """
        Updates a blog post.
        """
        data = request.json
        update_post(post, data)
        return None, 204

    @api.response(204, 'Post successfully deleted.')
    def delete(self, id):
        post = self.get_by_id(id)

        """
        Deletes blog post.
        """
        delete_post(post)

        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class PostsArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_blog_posts)
    def get(self, year, month=None, day=None):
        """
        Returns list of blog posts from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        posts_query = Post.query.filter(Post.pub_date >= start_date).filter(Post.pub_date <= end_date)

        posts_page = posts_query.paginate(page, per_page, error_out=False)

        return posts_page