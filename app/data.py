from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

file_path = r"C:\Users\avram\OneDrive\Desktop\TRG Week 35\pep.us.txt"

@app.route('/')
def load_dataframe():
    try:
        # Load data with parsing dates
        df = pd.read_csv(file_path, sep=",", engine="python", parse_dates=['Date'])
        
        # Drop OpenInt column if present
        if 'OpenInt' in df.columns:
            df = df.drop(columns=['OpenInt'])
        
        # Convert dataframe to HTML
        html_table = df.to_html(classes='table table-striped', index=False)

        # Render the dataframe inside a basic HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>PEP Data</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container mt-5">
                <h1>PEP DataFrame Preview</h1>
                {html_table}
            </div>
        </body>
        </html>
        """
        return render_template_string(html_template)
    except Exception as e:
        return f"An error occurred while loading the data: {e}"

if __name__ == '__main__':
    app.run(debug=True)
