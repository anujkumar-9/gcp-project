from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>GCP Multi Environment CI/CD</title>

<style>
body{
background:#0f172a;
color:white;
font-family:Arial;
text-align:center;
padding-top:120px;
}

.card{
width:700px;
margin:auto;
padding:40px;
background:#1e293b;
border-radius:20px;
box-shadow:0 0 30px rgba(0,0,0,.4);
}

h1{
color:#38bdf8;
}

p{
font-size:20px;
color:#cbd5e1;
}
</style>

</head>

<body>

<div class="card">

<h1>🚀 Multi Environment CI/CD Pipeline</h1>

<p>GitHub Actions → Artifact Registry → Cloud Run</p>

<p>Status: SUCCESS ✅</p>

</div>

</body>
</html>
"""

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)
