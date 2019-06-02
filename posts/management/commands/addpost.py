from django.core.management.base import BaseCommand, CommandError
from posts.models import Posts as Post

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('post_title', nargs='+', type=str)
        parser.add_argument('post_body', nargs='+', type=str)

    def handle(self, *args, **options):
        post_title = options["post_title"][0]
        post_body = options["post_body"][0]

        Post.objects.create(title=post_title, body=post_body)

        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % post_title))