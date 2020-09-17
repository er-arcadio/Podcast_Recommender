# This is where the python code goes

from flask import Flask, render_template, request, redirect
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from collections import defaultdict


app = Flask(__name__)


'''Opens the podcast vectors - podcasts as vectors'''
with open('podcast_vec.pkl', 'rb') as handle:
    podcast_vec = pickle.load(handle)

'''Opens the Word2Vec model - Turns search into vector'''
with open('w2v.pkl', 'rb') as handle:
    w2v = pickle.load(handle)

'''Opens the podcast title to ID reference'''
with open('title_ids.pkl', 'rb') as handle:
    PODCAST_IDS = pickle.load(handle)

USER_LIKES = defaultdict(list)   # key is user id : value is list of likes


def get_vectors(first_map, second_map):
    first_vec = dict()
    for key, value_list in first_map.items():
        temp = list()
        for element in value_list:
            try:
                temp.append(second_map[element])
            except KeyError:
                pass

        first_vec[key] = np.mean(temp, axis=0)

    return first_vec


def user_search(query, liked_podcasts=None):
    user_vec = get_vectors({'search': query.split(' ')}, w2v)

    if liked_podcasts:
        likes_dct = get_vectors({'likes': liked_podcasts}, podcast_vec)
        user_vec['likes'] = likes_dct['likes']

    return user_vec


def get_most_similar(podcast_vec, user_vec, likes=[]):
    sim = list()

    for key, vec in podcast_vec.items():
        thisSim = cosine_similarity(vec.reshape(1, -1), user_vec.reshape(1, -1))
        if key not in likes:
            sim.append((key, thisSim[0][0]))

    return sorted(sim, key=lambda x: x[1], reverse=True)


def get_website(podcast_title):
    id = PODCAST_IDS[podcast_title]
    ext = podcast_title.replace(' ', '-')
    website = f'https://www.thisamericanlife.org/{id}/{ext}'
    return website


def search_titles(query):
    titles = PODCAST_IDS.keys()
    return [[title, get_website(title)] for title in titles
            if set(query.lower().split()).intersection(set(title.lower().split()))]


def run_recommender(id, query):
    results = {
        'id': id,
        'query': query
    }

    # Checking for and Setting User Data from History
    try:
        users_likes = USER_LIKES[id]   # this
    except KeyError:
        users_likes = []

    users_likes = list(dict.fromkeys(users_likes))   # Prevents duplicate likes
    user_vec = user_search(query, liked_podcasts=users_likes)

    # Retrieving results with same key word
    results['search_results'] = search_titles(query)
    results_len = len(results['search_results'])

    # Retrieving the Search Results (cosine similar results)
    if results_len < 5 and query:
        search_tuples = get_most_similar(podcast_vec, user_vec['search'])[:5]
        cos_sim_search = [[result[0], get_website(result[0])] for result in search_tuples]
        for sim in cos_sim_search:
            if sim not in results['search_results'] and results_len < 5:
                results['search_results'].append(sim)
                results_len += 1
    else:
        results['search_results'] = results['search_results'][:5]

    # Retrieving recommendations using User Data
    try:
        rec_tuples = get_most_similar(podcast_vec, user_vec['likes'], likes=users_likes)[:5]
        results['recommendations'] = [(result[0], get_website(result[0])) for result in rec_tuples]
    except KeyError or IndexError:
        results['recommendations'] = []

    return results


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form['id']
        query = request.form['query']
        return redirect(f'/{id}/{query}')
    else:
        return render_template('index.html')


@app.route('/search/<string:id>', methods=['GET', 'POST'])
def search(id):
    if request.method == 'POST':
        query = request.form['search']
        query = query.replace('?search=', '')
        return redirect(f'/{id}/{query}')
    else:
        return redirect(f'/home')


@app.route('/<string:id>/', methods=['GET', 'POST'])
@app.route('/<string:id>/<string:query>', methods=['GET', 'POST'])
def user_query(id, query=''):
    results = run_recommender(id, query)

    try:
        like = request.form['like']
    except:
        like = None
    try:
        imported_id = request.form['id']
    except:
        imported_id = None
    try:
        query = request.form['query']
    except:
        pass

    if request.method == 'POST':
        if like:
            USER_LIKES[id].append(like)   #this
            id = id
            query = query
            return redirect(f'/{id}/{query}')
        if imported_id:
            id = imported_id
        else:
            id = id
        return redirect(f'/{id}/{query}')
    else:
        return render_template('posts.html', posts=results)


if __name__ == "__main__":
    app.run(debug=True)
