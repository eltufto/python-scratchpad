from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),                       
    url(r'^admin/', include(admin.site.urls)),
    url(r'^job_files/', include('job_files.urls'))
)
