#!/usr/bin/env python
# coding: utf-8

import markdown, re
from django import forms
from django.db.models import F
from blog.models import Blog
from django.contrib import admin

class BlogAdminForm(forms.ModelForm):
	class Meta:
		model = Blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'user', 'created']
	list_filter = ['user']
	form = BlogAdminForm

	def save_model(self, request, obj, form, change):
		'''新建/编辑 文章'''
		obj.user = request.user
		obj.content = markdown.markdown(obj.markdown)
		return super(BlogAdmin, self).save_model(request, obj, form, change)

	def delete_model(self, request, obj):
		'''删除文章'''
		ret = super(BlogAdmin, self).delete_model(request, obj)

admin.site.register(Blog, BlogAdmin)
