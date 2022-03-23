from django.shortcuts import render, HttpResponse
from books.models import Book

from django.utils.text import slugify


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all(), }
    return render(request, template, context)


def books_dates_view(request, pub_date):
    template = 'books/date_book.html'
    pagi_values = pagi(pub_date)
    values = Book.objects.get(pub_date=pub_date)
    context = {'book': values,
               'previos': pagi_values[0],
               'next': pagi_values[1]}
    return render(request, template, context)


def pagi(pub_date):
    books_dates = [d.pub_date for d in Book.objects.all()]
    books_dates.sort()
    books_dates = [slugify(d) for d in books_dates]
    index = books_dates.index(pub_date)
    if index == 0:
        a, b = '', books_dates[index + 1]
    elif index == len(books_dates) - 1:
        a, b = books_dates[index - 1], ''
    else:
        a, b = books_dates[index - 1], books_dates[index + 1]
    return a, b
