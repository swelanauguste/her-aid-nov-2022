from django.views.generic import TemplateView

from .models import Screening, SignAndPrevention, TypeOfAbuse


class Resource(TemplateView):
    types_of_abuse = TypeOfAbuse.objects.all()
    signs_and_preventions = SignAndPrevention.objects.all()
    questions = Screening.objects.all()
    extra_context = {
        "types_of_abuse": types_of_abuse,
        "signs_and_preventions": signs_and_preventions,
        "questions": questions,
    }
    template_name = "resources/resources.html"
