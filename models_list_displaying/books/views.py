from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books_list.html'
    books_list = Book.objects.all()
    context = {
        'books_list': books_list,
    }
    return render(request, template, context)

def date_list_books_view(request, date_url):
    template = 'date_list_books.html'
    data_list_books = Book.objects.all().filter(pub_date=date_url)

    list_dates = change_dates(date_url)
    context = {
        'data_list_books': data_list_books,
        'prev_page': list_dates[0],
        'next_page': list_dates[1]
    }
    return render(request, template, context)

def change_dates(date_url):
    list_books_by_data = Book.objects.order_by("pub_date")
    date_in = date_url.date()

    list_dates = [False, False]
    flag_first = True
    for i in range(len(list_books_by_data)):
        a = list_books_by_data[i].pub_date
        if a == date_in and flag_first:
            flag_first = False
            if i == 0:
                pass
            else:
                list_dates[0] = list_books_by_data[i-1].pub_date.isoformat()
        elif a != date_in and not flag_first:
            list_dates[1] = list_books_by_data[i].pub_date.isoformat()
            break
    return list_dates

