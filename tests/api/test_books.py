
class TestBooksApi:

    URL = "/api/books"

    EXPCTED_DATA = {
        'data': [
            {
                'author': 'Mrs. John Doe',
                'published': '2014-12-14T00:00:00.000Z',
                'title': 'Eloquent JavaScript, Second Edition'
            },
            {
                'author': 'Prof. John Doe',
                'published': '2012-07-01T00:00:00.000Z',
                'title': 'Learning JavaScript Design Patterns'
            },
            {
                'author': 'Prof. Jane Doe',
                'published': '2014-02-01T00:00:00.000Z',
                'title': 'Speaking JavaScript'
            },
            {
                'author': 'Mr. John Doe',
                'published': '2014-07-01T00:00:00.000Z',
                'title': 'Programming JavaScript Applications'
            },
            {
                'author': 'Dr. John Doe',
                'published': '2016-09-03T00:00:00.000Z',
                'title': 'Understanding ECMAScript 6'
            },
            {
                'author': 'Dr. Jane Doe',
                'published': '2015-12-27T00:00:00.000Z',
                'title': "You Don't Know JS"
            },
            {
                'author': 'Mr. Jane Doe',
                'published': '2013-08-02T00:00:00.000Z',
                'title': 'Git Pocket Guide'
            },
            {
                'author': 'Prof. John Doe',
                'published': '2014-04-07T00:00:00.000Z',
                'title': 'Designing Evolvable Web APIs with ASP.NET'
            },
            {
                'author': 'Honoré de Balzac',
                'published': '1844-01-01T00:00:00.000Z',
                'title': 'Un début dans la vie'
            },
            {
                'author': 'Honoré de Balzac',
                'published': '1835-01-01T00:00:00.000Z',
                'title': 'Le père Goriot'}
        ]
    }

    def test_get_book_collection(self, client):
        response = client.get(self.URL)
        assert response.status_code == 200
        assert response.json['data'] == self.EXPCTED_DATA['data']

    def test_get_book_collection_sort_by_title_desc(self, client):
        response = client.get(self.URL + "?sort_by=title&order=desc")
        assert response.status_code == 200
        exp_data = sorted(self.EXPCTED_DATA['data'], key=lambda x: x['title'], reverse=True)
        assert response.json['data'] == exp_data

    def test_get_book_collection_sort_by_title_asc(self, client):
        response = client.get(self.URL + "?sort_by=title&order=asc")
        assert response.status_code == 200
        exp_data = sorted(self.EXPCTED_DATA['data'], key=lambda x: x['title'])
        assert response.json['data'] == exp_data

    def test_get_book_collection_sort_by_title_asc_by_default(self, client):
        response = client.get(self.URL + "?sort_by=title")
        assert response.status_code == 200
        exp_data = sorted(self.EXPCTED_DATA['data'], key=lambda x: x['title'])
        assert response.json['data'] == exp_data

    def test_get_book_collection_sort_by_date_asc(self, client):
        response = client.get(self.URL + "?sort_by=published&order=asc")
        assert response.status_code == 200
        exp_data = sorted(self.EXPCTED_DATA['data'], key=lambda x: x['published'])
        assert response.json['data'] == exp_data

    def test_get_book_collection_sort_by_date_desc(self, client):
        response = client.get(self.URL + "?sort_by=published&order=desc")
        assert response.status_code == 200
        exp_data = sorted(self.EXPCTED_DATA['data'], key=lambda x: x['published'], reverse=True)
        assert response.json['data'] == exp_data

    def test_get_book_collection_sort_by_invalid_field(self, client):
        response = client.get(self.URL + "?sort_by=fake_field_name&order=desc")
        assert response.status_code == 200
        assert response.json['data'] == self.EXPCTED_DATA['data']

    def test_get_book_collection_invalid_order_field(self, client):
        response = client.get(self.URL + "?sort_by=title&order=fake_order")
        assert response.status_code == 200
        assert response.json['data'] == self.EXPCTED_DATA['data']
