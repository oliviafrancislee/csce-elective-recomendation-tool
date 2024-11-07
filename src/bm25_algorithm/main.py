""" import bm25

def main():
    i = input("List your interests separated by commas: ")
    print(bm25.BM25(i))

if __name__ == "__main__":
    main()

""" 
from flask import Flask, request, jsonify
from flask_cors import CORS
import bm25

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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

if __name__ == "__main__":
    app.run(debug=True)