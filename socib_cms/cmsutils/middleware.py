 # coding: utf-8
from django import http
from django.utils.deprecation import MiddlewareMixin


class FilterPersistMiddleware(MiddlewareMixin):
    """Middleware adapted from https://code.djangoproject.com/ticket/3777#comment%3A4
    """

    def process_request(self, request):
        path = request.path
        if path.find('/admin/') != -1:  # Dont waste time if we are not in admin
            query_string = request.META['QUERY_STRING']
            if 'HTTP_REFERER' not in request.META:
                return None

            session = request.session
            if session.get('redirected', False):  # so that we dont loop once redirected
                del session['redirected']
                return None

            referrer = request.META['HTTP_REFERER'].split('?')[0]
            referrer = referrer[referrer.find('/admin'):len(referrer)]
            key = 'key' + path.replace('/', '_')

            if path == referrer:
                # We are in same page as before
                if query_string == '':
                    # Filter is empty, delete it
                    if session.get(key, False):
                        del session[key]
                    return None
                request.session[key] = query_string
            else:
                # We are are coming from another page, restore filter if available
                if session.get(key, False):
                    query_string = request.session.get(key)
                    redirect_to = path + '?' + query_string
                    request.session['redirected'] = True
                    return http.HttpResponseRedirect(redirect_to)
                else:
                    return None
        else:
            return None
