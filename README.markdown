Django Facebook Utils
=====================

**License:** MIT

The intent of this project is to provide some very basic utilities related to Facebook.

At the moment there are only two features:

* An utility that forces the update of an URL in the Facebook's share cache.
* A Context Processor that allows you to hide Facebook [Open Graph Protocol](http://developers.facebook.com/docs/opengraphprotocol/) &lt;meta&gt; tags from other User Agents.


Test it
=======

````bash
# Download and install example
cd /tmp
virtualenv testfacebookutils
cd testfacebookutils
git clone https://github.com/caioariede/django-facebook-utils.git
source bin/activate
cd django-facebook-utils/example
pip install -r requirements.txt

# Test
./manage.py ping_facebook http://example.com --verbosity=2
````

Installation
------------

`pip install django-facebook-utils` or install the master branch:

`pip install git+http://github.com/caioariede/django-facebook-utils.git#egg=facebook_utils`


How to force an URL to be updated from Facebook's cache
-------------------------------------------------------

1. The `ping_facebook` command:

	`python manage.py ping_facebook http://example.com`
	
	See below **How to extend the ping_facebook command** to fit your needs.

2. Calling the `ping_facebook` shortcut:

		from facebook_utils.shortcuts import ping_facebook
		
		if ping_facebook('http://example.com'):
			print('success')
		else:
			print('fail')
	
	This shortcut will only return `True` or `False`. If you need more information to debug, you can call `facebook_utils.utils.ping` or use the `ping_facebook` command with `--verbosity=2` (more verbose).

Detecting Facebook requests
---------------------------

1. The `facebookexternalhit` context processor (for templates):

	Add `facebook_utils.context_processors.facebookexternalhit` to the [TEMPLATE_CONTEXT_PROCESSOR](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS) setting in `settings.py`:
	
        TEMPLATE_CONTEXT_PROCESSORS = (
            #  .. other stuff
            'facebook_utils.context_processors.facebookexternalhit',
        )

	In the template:
	
		{% if facebookexternalhit %}
    		<meta property="og:title" content="The Rock"/>
    		<meta property="og:type" content="movie"/>
    		<meta property="og:url" content="http://www.imdb.com/title/tt0117500/"/>
    		<meta property="og:image" content="http://ia.media-imdb.com/rock.jpg"/>
    	{% endif %}

2. The `is_facebookexternalhit` shortcut:

		from facebook_utils.shortcuts import is_facebookexternalhit
		
		def some_view(request):
			if is_facebookexternalhit(request):
				return HttpResponse('Hello, Facebook!')
			return HttpResponse('Hello visitor!')

How to extend the ping_facebook command
---------------------------------------

You can easily extend the `ping_facebook` command to fit your needs.

1. First of all, [start writing your own custom command](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/).
2. Now extends the `ping_facebook` command:

		from facebook_utils.management.commands import BasePingCommand
		
3. Finally, extend it to fit your needs:

        class Command(BasePingCommand):
            help = 'Ping some pages stored in database'

            def handle(self, **options):
                verbosity = options.get('verbosity')
                traceback = options.get('traceback')
                
                for page in Page.objects.all():
                    page_url = page.get_absolute_url()
                    self.do_ping(page_url, verbosity, traceback)
