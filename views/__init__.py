import numpy as np
import pandas as pd
from flask import Blueprint, render_template, request

base = Blueprint('base', __name__)
books = pd.read_csv('./books.csv').fillna(1)


@base.route('/')
def index():
    books = pd.read_csv('~/workspaces/Collage/spk/dataset/books.csv').fillna(1)
    return render_template('index.html', books=books[:100])


@base.route('/calculate', methods=['post'])
def calculate():
    books = pd.read_csv('./books.csv').fillna(1)[:100]
    isMaxRate = request.form.get('max-rate', 'off') == "on"
    isMaxYear = request.form.get('max-year', 'off') == "on"
    yearWeight = request.form['year-weight']
    rateWeight = request.form['rate-weight']

    bookRates = np.array(books[['average_rating']])
    bookYears = np.array(books[['original_publication_year']])

    weights = np.array([[int(rateWeight), int(yearWeight)]]) / 100

    rateNorm = bookRates / bookRates.max() if isMaxRate else bookRates.min() / bookRates
    yearNorm = bookYears / bookYears.max() if isMaxYear else bookYears.min() / bookYears
    normalized = np.concatenate((rateNorm, yearNorm), axis=1)

    V = np.matmul(normalized, weights.transpose())
    books['V'] = V
    books = books.sort_values(by=['V'], ascending=False)
    return render_template('result.html', books=books[:3], yearWeight=yearWeight, rateWeight=rateWeight,
                           isMaxRate=('minimalkan', 'maksimalkan')[isMaxRate], isMaxYear=('minimalkan', 'maksimalkan')[isMaxYear])
