from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

file_path = r"C:\Users\avram\OneDrive\Desktop\TRG Week 35\pep.us.txt"

# Load and preprocess data once at startup
df_master = pd.read_csv(file_path, sep=",", engine="python", parse_dates=['Date'])

if 'OpenInt' in df_master.columns:
    df_master = df_master.drop(columns=['OpenInt'])

df_77_89 = df_master[(df_master['Date'] >= '1977-01-01') & (df_master['Date'] <= '1989-12-31')]
df_90_99 = df_master[(df_master['Date'] >= '1990-01-01') & (df_master['Date'] <= '1999-12-31')]
df_00_17 = df_master[(df_master['Date'] >= '2000-01-01') & (df_master['Date'] <= '2017-11-10')]

def render_table(df, title):
    html_table = df.to_html(classes='table table-striped', index=False)
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1>{title}</h1>
            {html_table}
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

@app.route('/')
def show_77_89():
    return render_table(df_77_89, "PEP Data: 1977–1989")

@app.route('/90_99')
def show_90_99():
    return render_table(df_90_99, "PEP Data: 1990–1999")

@app.route('/00_17')
def show_00_17():
    return render_table(df_00_17, "PEP Data: 2000–2017")

if __name__ == '__main__':
    app.run(debug=True)
