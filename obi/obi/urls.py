from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ui.views',

    url(r'^$', 'home', name='home'),
    url(r'^everything$', 'everything', name='everything'),

    url(r'^databases_html', 'databases_html', name='databases_html'),
    url(r'^databases_json', 'databases_json', name='databases_json'),

    url(r'^databases_solr_html', 'databases_solr_html',
        name='databases_solr_html'),
    url(r'^databases_solr_json', 'databases_solr_json',
        name='databases_solr_json'),

    url(r'^journals_html', 'journals_html', name='journals_html'),
    url(r'^journals_json', 'journals_json', name='journals_json'),

    url(r'^journals_solr_html', 'journals_solr_html',
        name='journals_solr_html'),
    url(r'^journals_solr_json', 'journals_solr_json',
        name='journals_solr_json'),

    url(r'^summon_html', 'summon_html', name='summon_html',
        kwargs={'scope': 'all'}),
    url(r'^summon_json', 'summon_json', name='summon_json',
        kwargs={'scope': 'all'}),

    url(r'^articles_html', 'summon_html', name='articles_html',
        kwargs={'scope': 'articles'}),
    url(r'^articles_json', 'summon_json', name='articles_json',
        kwargs={'scope': 'articles'}),

    url(r'^books_media_html', 'books_media_html',
        name='books_media_html'),
    url(r'^books_media_json', 'books_media_json',
        name='books_media_json'),

    url(r'^launchpad_html', 'launchpad_html',
        name='launchpad_html'),
    url(r'^launchpad_json', 'launchpad_json',
        name='launchpad_json'),

    url(r'^summon_books_media_html', 'summon_html',
        name='summon_books_media_html', kwargs={'scope': 'books_media'}),
    url(r'^summon_books_media_json', 'summon_json',
        name='summon_books_media_json', kwargs={'scope': 'books_media'}),

    url(r'^research_guides_html', 'summon_html',
        name='research_guides_html', kwargs={'scope': 'research_guides'}),
    url(r'^research_guides_json', 'summon_json',
        name='research_guides_json', kwargs={'scope': 'research_guides'}),

    url(r'^best_bets_html', 'summon_html',
        name='best_bets_html', kwargs={'scope': 'best_bets'}),
    url(r'^best_bets_json', 'summon_json',
        name='best_bets_json', kwargs={'scope': 'best_bets'}),

    url(r'^libsite_html', 'libsite_html', name='libsite_html'),
    url(r'^libsite_json', 'libsite_json', name='libsite_json'),

    url(r'^summon_healthcheck_json', 'summon_healthcheck_json',
        name='summon_healthcheck_json'),

    url(r'^searches', 'searches', name='searches'),
    url(r'^save_data', 'save_data', name='save_data'),
)

urlpatterns += patterns('',

    url(r'^admin/', include(admin.site.urls)),

)
