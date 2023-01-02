from .models import Posts


def most_view(request):
    p = Posts.objects.all()
    context = {}
    context["most_view"] = p.order_by("-views")[:5]
    return context