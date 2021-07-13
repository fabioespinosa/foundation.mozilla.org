from django.core.management.base import BaseCommand

from networkapi.wagtailpages.models import BlogPage


class Command(BaseCommand):
    help = '''
        Ensures that all blog posts have three explicit related posts,
        rather than relying on the "find related posts for a blog post"
        function every time the blog page is requested by a user.
    '''

    def handle(self, *args, **options):
        all_posts = BlogPage.objects.all()
        total_posts = all_posts.count()

        print('Total number of posts  update:', total_posts)

        for i, post in enumerate(all_posts):
            print(f"Processing posts {i+1} out of {total_posts}")
            post.ensure_related_posts()
            post.save_revision().publish()
