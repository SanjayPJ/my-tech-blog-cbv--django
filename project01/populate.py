
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mysite.settings')

import django
django.setup()

import random
from blog.models import Post
from faker import Faker

from django.contrib.auth.models import User

user = User.objects.create_user('myusername04', 'myemail@crazymail.com', 'mypassword')

fakegen = Faker()

for i in range(10):
    fake_author = user
    fake_title = fakegen.paragraph()
    fake_text = fakegen.paragraph(nb_sentences=140, variable_nb_sentences=True, ext_word_list=None)
    post = Post.objects.get_or_create(user = fake_author, title = fake_title, body = fake_text, published_date=fakegen.date())