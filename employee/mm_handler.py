# Parser for data from frontend, for classes have many to many foreign key fields.
from publication_details.models import Book


def handler(kls, data):
    print('Inside Handler')

    if kls == 'Book':
        for d in data:
            print(d)
            pk = d.pop('pk')
            d.pop('model')
            authors = d.pop('author')
            b = Book.objects.filter(id=pk).update(**d)

