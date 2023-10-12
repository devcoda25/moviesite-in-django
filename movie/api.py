import requests


from django.core.paginator import Paginator

def movie_data(request):
    movie_url = "https://yts.mx/api/v2/list_movies.json"
    params = {
        'limit': 20,
        'page': request.GET.get('page', 1),
        'quality': '720p',
        'minimum_rating': 7,
        'query_term': request.GET.get('query_term', ''),
        'genre': 'action',
        'sort_by': 'year',
        'order_by': 'desc',
        'with_rt_ratings': 'true',
    }
    response = requests.get(movie_url, params=params)
    data = response.json()
    movies = data['data']['movies']
    paginator = Paginator(movies, 20)  # Show 20 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {'movies': page_obj}



def movie_data(request):
    movie_url = "https://yts.mx/api/v2/list_movies.json"
    response = requests.get(movie_url)
    data = response.json()
    movies = data['data']['movies'][:4]  # Fetch only the first 6 movies
    return {'movies': movies}


# context_processors.py

# def yts_movies(request):
#     query_term = 'your_query_term'  # Replace this with the actual query term
#     response = requests.get(f'https://yts.mx/api/v2/list_movies.json?query_term={query_term}')
#     data = response.json()
#     return {'movies': data['data']['movies'], 'movie_count': data['data']['movie_count'], 'limit': data['data']['limit'], 'page_number': data['data']['page_number']}


def movie_list(request, page_number=1):
    query_term = '3D'  # Replace this with the actual query term
    response = requests.get(f'https://yts.mx/api/v2/list_movies.json?query_term={query_term}')
    data = response.json()
    movies = data['data']['movies']
    paginator = Paginator(movies, data['data']['limit'])
    page_obj = paginator.get_page(page_number)
    return {'page_obj': page_obj, 'movie_count': data['data']['movie_count']}

def movie_details(request, movie_id=None):
    if movie_id is None:
        return {'movie_details': {}}
        
    url = 'https://yts.mx/api/v2/movie_details.json'
    params = {'movie_id': movie_id}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {'movie_details': data}
    else:
        return {'error': f'Request failed with status code {response.status_code}'}
