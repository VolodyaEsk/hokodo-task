from flask import request, jsonify, render_template
import requests

from app import app


URL = 'https://hokodo-frontend-interview.netlify.com/data.json'
DATA = requests.get(URL).json()


@app.route('/api/books')
def books():

    sort_by = request.args.get('sort_by')
    order = request.args.get('order', 'asc').lower()

    books = []
    for book in DATA['books']:
        book_data = dict(
            author=book.get('author'),
            published=book.get('published'),
            title=book.get('title')
        )
        books.append(book_data)

    if sort_by:
        sort_by = sort_by.lower()
        if sort_by in ['title', 'published']:
            if order == 'asc':
                books.sort(key=lambda x: x[sort_by])
            elif order == 'desc':
                books.sort(key=lambda x: x[sort_by], reverse=True)

    return jsonify({"data": books})


@app.route('/api/authors')
def authors():

    authors = {}

    for book in DATA['books']:
        author = book['author']
        authors.setdefault(author, []).append(book['title'])

    return jsonify({"data": authors})


