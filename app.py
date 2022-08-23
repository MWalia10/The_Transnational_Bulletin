from flask import Flask, render_template
import csv

app = Flask(__name__)

def data(path):
    language_data = []
    first_line = True
    n = 3
    with open(path, encoding="utf8") as csv_file:
        data = csv.reader(csv_file, delimiter='\t')
        for row in data:
            if not first_line:
                language_data.append({
                    "Title": row[n - 2],
                    "Eng_Title": row[n],
                    "Eng_Des": row[n + 1],
                    "url": row[n + 2]
                    })
            else:
                first_line = False
    return language_data        

def data_i(path):
    language_data = []
    first_line = True
    n = 1
    with open(path, encoding="utf8") as csv_file:
        data = csv.reader(csv_file, delimiter='\t')
        for row in data:
            if not first_line:
                language_data.append({
                    "Eng_Title": row[n],
                    "Eng_Des": row[n + 1],
                    "url": row[n + 2],
                    "Title": row[n + 3]
                    })
            else:
                first_line = False
    return language_data  

@app.route('/')
def home():
    arabic = data("Arabic.tsv")
    spanish = data("Argentina.tsv")
    french = data("French.tsv")
    indian = data_i("India.tsv") 
    russian = data("Russian.tsv")
    
    return render_template(
        "home.html", arabic_main = arabic[0], arabic_list = arabic[1:], spanish_main = spanish[0], spanish_list = spanish[1:],
        french_main = french[0], french_list = french[1:], indian_main = indian[0], indian_list = indian[1:],
        russian_main = russian[0], russian_list = russian[1:])

if __name__ == "__main__":
    app.run(debug = True)