import pandas as pd
from flask import Flask, request
app = Flask(__name__)

#Creating a first POST point!!
@app.route('/PGwodehouse', methods=['POST']) 
def PG():
    data = pd.read_csv('PGwodehouse.csv')
    return (data.to_json())

#mendapat nama author
@app.route('/PGwodehouse')
def PGwodehouse():
    data = pd.read_csv('data/PGwodehouse.csv')
    return data.to_json()

@app.route('/Agatha_Christie')
def AgathaChrst():
    data = pd.read_csv('data/book_author.csv')
    return data.to_json()

##EDA##
# get a missing value in a df
@app.route('/missval')
def miss_val():
    data = pd.read_csv('data/missval.csv')
    return data.to_json()

#categorical value
@app.route('/language_category')
def language_cat():
    data = pd.read_csv('data/language_cat.csv')
    return data.to_json()

#Rating frequency from book_author df
@app.route('/rating_frequency')
def freq_rate():
    data = pd.read_csv('data/freq_rating.csv')
    return data.to_json()

#Stack / unstack
@app.route('/author_stack')
def Stack():
    data = pd.read_csv('data/author_stack.csv')
    return data.to_json()

@app.route('/author_unstack')
def un_Stack():
    data = pd.read_csv('data/unstack_author.csv')
    return data.to_json()

#Group by
@app.route('/group_languange')
def Group():
    data = pd.read_csv('data/language_group.csv')
    return data.to_json()

#minimum join 4 table from DF
@app.route('/4Table')
def table():
    data = pd.read_csv('data/choosen_table.csv')
    return data.to_json()

# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<PGwodehouse>/<isbn>/<value>', methods=['GET']) 
def get_data_equal(PGwodehouse,isbn,value):
    code = value
    book = pd.read_csv('data/' + str('PGwodehouse.csv'))
    mask = book['isbn'] == code
    book = book[mask]
    return (book.to_json())

@app.route('/data/get/<Agatha_Christie>/<isbn>/<value>', methods=['GET']) 
def get_data(Agatha_Christie,isbn,value):
    code = value
    book = pd.read_csv('data/' + str('book_author.csv'))
    mask = book['isbn'] == code
    book = book[mask]
    return (book.to_json())

@app.route('/data/get/lang/<Agatha_Christie>/<language>/<value>', methods=['GET']) 
def get_data_lang(Agatha_Christie,language,value):
    name = value
    authr = pd.read_csv('data/' + str('book_author.csv'))
    language = authr['language_code'] == name
    authr = authr[language]
    return (authr.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000