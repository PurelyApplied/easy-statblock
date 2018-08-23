from django.http import HttpResponse


# class IndexView(generic.ListView):
#     template_name = 'converter/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]

def index(request):
    return HttpResponse("Hello, world.")
