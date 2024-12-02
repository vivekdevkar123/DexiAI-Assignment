from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper import scrape_jobs

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# List of allowed keywords
ALLOWED_KEYWORDS = (
    "software-engineer", "engineering-manager", "artificial-intelligence-engineer",
    "machine-learning-engineer", "product-manager", "backend-engineer", 
    "mobile-engineer", "product-designer", "frontend-engineer", 
    "full-stack-engineer", "data-scientist", "designer", 
    "software-architect", "devops-engineer"
)

@app.route("/scrape", methods=["GET"])
def get_jobs():
    """Endpoint to trigger the scraper and return job data."""
    keyword = request.args.get("keyword", "").strip()
    
    # Validate keyword
    if keyword not in ALLOWED_KEYWORDS:
        return jsonify({"error": f"Invalid keyword. Allowed keywords are: {', '.join(ALLOWED_KEYWORDS)}"}), 400

    try:
        jobs = scrape_jobs(keyword)  # List of dictionaries
        print(jobs)
        if not jobs:
            return jsonify({"error": "No jobs found for the specified keyword."}), 404
        return jsonify(jobs), 200  # Directly return the list
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
