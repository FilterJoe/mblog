from django.shortcuts import render_to_response
from django.template import RequestContext # to get my css file to be seen


def homepage(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))