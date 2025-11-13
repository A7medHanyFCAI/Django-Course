from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import random
from .models import Book
from .tasks import long_task_one, long_task_two

def manual_cache_view(request):
    books = cache.get("books_list")

    if not books:
        print("Fetching from DB")
        books = list(Book.objects.all())
        cache.set("books_list", books, timeout=30)  
    else:
        print("Loaded from cache")

    return render(request, "books/manual_cache.html", {"books": books})



@cache_page(20)  
def view_cache_view(request):
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "Simplicity is the soul of efficiency.",
        "Before software can be reusable it first has to be usable.",
        "Make it work, make it right, make it fast.",
        "Talk is cheap. Show me the code."
    ]
    random_quote = random.choice(quotes)
    context = {"quote": random_quote}
    return render(request, "books/view_cache.html", context)

def query_cache_view(request):
    cache_key = "query_books"
    books = cache.get(cache_key)
    if not books:
        print("Fetching from DB")
        books = list(Book.objects.all().values("title", "author", "price"))
        cache.set(cache_key, books, timeout=60)
    else:
        print("Loaded from cache")

    return render(request, "books/query_cache.html", {"books": books})


def template_cache_view(request):
    books = Book.objects.all()
    return render(request, "books/template_cache.html", {"books": books})


def trigger_tasks(request):
    long_task_one.delay()
    long_task_two.delay()
    return render(request, "books/task_trigger.html", {"message": "Tasks sent to Celery!"})