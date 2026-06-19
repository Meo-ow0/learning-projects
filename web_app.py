import os
from flask import Flask, request
from app import extract_data  # This connects the two files!

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        if not os.path.exists("uploads"): os.makedirs("uploads")
        path = os.path.join("uploads", file.filename)
        file.save(path)
        
        result = extract_data(path) # Calls the logic from app.py
        return f"<h1>Result:</h1><pre>{result}</pre><br><a href='/'>Upload another</a>"
    
    return '''
        <h1>DocFlow AI</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload and Process">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)