from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "homepage.html"


# def home_page(request):
#     return render_to_response('homepage.html', context_instance=RequestContext(request))


