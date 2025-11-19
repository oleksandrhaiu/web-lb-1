from django.http import HttpResponse


def index(request):
    """
    Копія view з магазину, але з іншим текстом.
    Це показує, що проєкт може містити кілька незалежних застосунків.
    """
    return HttpResponse("Каталог товарів працює! Це другий застосунок.")
