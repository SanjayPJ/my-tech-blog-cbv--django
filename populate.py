
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'my_tech_blog.settings')

import django
django.setup()

import random
from django.template.defaultfilters import slugify
from blog.models import Post, Comment
from faker import Faker

from django.contrib.auth.models import User

user = User.objects.create_user('myusername2', 'myemail@crazymail.com', 'mypassword')

fakegen = Faker()

for i in range(10):
    fake_author = user
    fake_title = fakegen.paragraph()
    fake_text = fakegen.paragraph(nb_sentences=40, variable_nb_sentences=True, ext_word_list=None)

    post = Post.objects.get_or_create(author = fake_author, title = fake_title, text = fake_text, published_date=fakegen.date())
