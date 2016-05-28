#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------
# email  : gengjie@outlook.com
# Create Time: 5/24/16 22:49
# ----------------------------------------

from django.conf.urls import url
from .views import index, check, userpage


urlpatterns = [
    url(r'^$', index),
    url(r'^check/$', check),
]
