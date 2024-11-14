""" import bm25

def main():
    i = input("List your interests separated by commas: ")
    print(bm25.BM25(i))

if __name__ == "__main__":
    main()

""" 
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import bm25

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'src/UI/search.html')

@app.route('/bm25', methods=['GET'])
def bm25_endpoint():
    course_code = request.args.get('course_code')  # Get the query from the URL
    results = bm25.BM25('software')  # Call your BM25 function with the query
    
    print(f"Query: {course_code}")

    # Extract course information based on the class code
    course_info = {}
    for category, courses in results.items():
        for (course_code_result, course_name), details in courses.items():
            if course_code_result.strip() == course_code.strip():
                course_info = {
                    'course_code': course_code_result,
                    'course_name': course_name,
                    'credits': details['desc'][0],
                    'description': details['desc'][1]
                }
                break

    print(f"Query: {course_code}, Course Info: {course_info}")  # Debugging line
    return jsonify(course_info)

@app.route('/tracked', methods=['GET'])
def tracked_endpoint():
    q = request.args.get('query')  # Get the query from the URL
    results = bm25.BM25(q)  # Call your BM25 function with the query

    # Extract course information based on the class code
    tracked_electives = {}
    for category, courses in results.items():
        tracked_electives[category] = []
        for (course_code, course_name), details in courses.items():
            tracked_electives[category].append(course_code + " " + course_name)
    return jsonify(tracked_electives)

@app.route('/untracked', methods=['GET'])
def untracked_endpoint():
    q = request.args.get('query')  # Get the query from the URL
    results = bm25.BM25_untracked(q)  # Call your BM25 function with the query

    # Extract course information based on the class code
    untracked_electives = []
    for (course_code, course_name) in results:
        untracked_electives.append(course_code + " " + course_name)
    
    print(untracked_electives)
    return jsonify(untracked_electives)

""" 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT provided by Heroku, or default to 5000 for local testing
    app.run(debug=True, host="0.0.0.0", port=port)
 """

if name == 'main':
    app.run(debug=True, host='0.0.0.0', port=8080)