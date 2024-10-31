# CSCE Elective Recommendation Tool

# Overview
This tool recommends CSCE electives based on a custom BM25-based ranking algorithm. It includes data cleaning functions to process course catalog data and calculate term frequencies. The BM25 algorithm computes scores to   identify the most relevant elective courses for a given query.

# Setup Instructions

# Prerequisites    
- Python 3.x
- NO DEPENDENCIES

# Installation
Clone the Repository
Clone the project repository to your local machine:

      git clone https://github.com/yourusername/csce-elective-recommendation-tool.git
      cd csce-elective-recommendation-tool

Directory Structure
    
    src/
    ├── bm25_algorithm/
    │   ├── bm25.py            # BM25 algorithm logic
    │   ├── data.py            # Data cleaning functions for electives and catalog
    │   └── main.py            # Script to execute BM25 query and output recommendations
    data/
    ├── tracked_elective_list.txt # List of electives grouped by track
    └── course_catalog.txt        # Catalog with descriptions and prerequisites
    
Running the Code
    Prepare the Data
    Ensure the elective list (tracked_elective_list.txt) and course catalog (course_catalog.txt) files are in the data/ directory.
    Execute the Script
    From the root directory, run the following command:   
    
    python3 .\src\bm25_algorithm\main.py

   When prompted with "List your interests separated by commas:", enter a comma-separated list of your interests and press enter.

    Ex. "software engineering, web design, python"
    
   The program will output a dictionary where each track name is mapped to a ranked list of courses. Each course entry will include the course name, BM25 score, and a brief description.
