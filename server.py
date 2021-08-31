from flask import Flask
from flask import jsonify
from flask import render_template
from waitress import serve

app = Flask(__name__)
@app.route('/tests/first')
def output():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>first test</title>
</head>
<body>
    <div style="border-radius: 25px;
    background: #0f0;
    padding: 20px;
    width: 200px;
    height: 150px;">
        <p style="font-family: sans-serif;">This is the first test.</p>
    </div>
</body>
</html>'''

serve(app, host='0.0.0.0', port=8080, threads=1) #WAITRESS!