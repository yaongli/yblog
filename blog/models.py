# coding: utf-8

import markdown
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Blog(models.Model):
    '''Blog'''
    title = models.CharField(max_length=255, db_index=True, verbose_name=u'标题')
    user = models.ForeignKey(User, verbose_name=u'作者')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'日期', editable=False, db_index=True)
    markdown = models.TextField(verbose_name=u'内容')
    content = models.TextField(blank=True, null=True, editable=False)
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        self.content = markdown.markdown(self.markdown)
        super(Blog, self).save() # Call the "real" save() method.
        return self
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = verbose_name = u'Blog'
        
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        #exclude = ("created", "content")
        fields = ('title', 'markdown')
