from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Symon's EKS GitOps Deployment</h1>
    <p>Deployed successfully with GitHub Actions, Amazon ECR, Helm and ArgoCD!</p>
    <p>Version: v2</p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
