# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models

# import tagging
# from tagging.fields import TagField
# from tagging.models import Tag

class Category(models.Model):
    categ = models.TextField( blank=True, null=True )

    def __unicode__(self):
        return self.categ

    def get_categories(self):
        """return categories
        """
        tags = Category.objects.all()
        return set([t.categ for t in tags])

    def get_categs(self):
        """return 
        Arguments:
        - `self`:
        """
        return Category.objects.values_list('categ', flat=True)


class Posts(models.Model):
    header = models.TextField( blank = True )
    post = tinymce_models.HTMLField( blank = True )
    prepost = tinymce_models.HTMLField( blank = True )
    date_pub = models.DateField( auto_now_add = True )
    tags = models.TextField( blank=True )
    categories = models.ForeignKey(Category)
    flag_enabled = models.BooleanField()

    def __unicode__(self):
        return self.header

    def get_posts(self):
        """return posts
        """
        return Posts.objects.all()

    def get_post(self, url_post):
        """return post
        """
        return Posts.objects.get(id = url_post)

    def get_tags(self):
        """return tags list
        """
        tags = Posts.objects.all()
        list_tags = [[t.id, t.tags.split(',')] for t in tags]
        return list_tags

    def cloud_tags(self):
        """return all tags in one number
        """
        cloud_tag = []
        tags = Posts.objects.all()
        for i in tags:
            list_tags = i.tags.split(',')
            for p in list_tags:
                if p in cloud_tag:
                    pass
                else:
                    cloud_tag.append(p)
        return sorted(cloud_tag)

    def get_posts_tag(self, url_tag):
        """return posts from one tag
        """
        return Posts.objects.filter(tags__contains=url_tag)

    def get_tag_to_post(self, id_post):
        """return tags for one post
        """
        tags = Posts.objects.get(id=id_post)
        list_tags = tags.tags.split(',')
        # assert False
        return list_tags

    def get_posts_categ(self, categ):
        """return posts fron id_categ
        Arguments:
        - `self`:
        - `id_categ`: id category
        """
        return Posts.objects.filter(categories__categ=categ)

    class Meta:
        ordering = ["-date_pub"]

class Tags(models.Model):
    tags = models.TextField( blank=True, null=True )
    flag_enabled = models.BooleanField()

    def __unicode__(self):
        return self.categ
