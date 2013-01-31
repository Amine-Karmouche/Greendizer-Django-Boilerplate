from django.conf.urls import patterns, include, url
from GDb import auth_page, main_page

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', auth_page),
    (r'^login/app/$', main_page),
    # Examples:
    # url(r'^$', 'GDb.views.home', name='home'),
    # url(r'^GDb/', include('GDb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
