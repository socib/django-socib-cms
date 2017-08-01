# coding: utf-8

from django.http import HttpResponse
import mimetypes
import json
import urllib2


def proxy_to(request, path, target_url):
    url = '%s%s' % (target_url, path)
    if 'QUERY_STRING' in request.META and request.META['QUERY_STRING']:
        url += '?' + request.META['QUERY_STRING']
    try:
        proxied_request = urllib2.urlopen(url)
        status_code = proxied_request.code
        mimetype = proxied_request.headers.typeheader or mimetypes.guess_type(url)
        content = proxied_request.read()
    except urllib2.HTTPError as e:
        return HttpResponse(e.msg, status=e.code, content_type='text/plain')
    else:
        return HttpResponse(content, status=status_code, content_type=mimetype)


class JSONResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(json.dumps(self.get_data(context)),
                            content_type='application/json',
                            **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        return context
