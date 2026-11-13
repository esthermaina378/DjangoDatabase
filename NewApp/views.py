from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from NewApp.models import Book
from NewApp.myform import BookForm


# Create your views here.
def showbooks(request):
    books = Book.objects.all()
    return render(request, 'showbooks.html', {'books': books})


def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('showbooks')

    else:
        form = BookForm()
    return render(request, 'addbook.html', {'form': form}) # Sending to frontend

 # Django models
 # Book.objects.create(title='River and the Source',
 #                        year=2021,
 #                        category='Fiction',
 #                        isbn='978-3-540-8915-6',
 #                        cost=450,
 #                        published=True)
 #    Book.objects.create(title='Blossoms',
 #                        year=2006,
 #                        category='Fiction',
 #                        isbn='978-3-540-9660-6',
 #                        cost=250,
 #                        published=True)
def delete_book(request, id):
    book = Book.objects.get(id=id) # select * from books where id = 34
    book.delete() # select from books where id = 3
    messages.success(request, "Book deleted successfully!")
    return redirect('show books')


def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book edited successfully!")
            return redirect('showbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'editbook.html', {'form': form})

# TODO image, login, register, django admin