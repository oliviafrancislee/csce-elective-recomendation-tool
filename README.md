# CSCE Elective Recommendation Tool

# Overview
This tool recommends CSCE electives based on a custom BM25-based ranking algorithm. It includes data cleaning functions to process course catalog data and calculate term frequencies. The BM25 algorithm computes scores to   identify the most relevant elective courses for a given query.

# Link
https://csce-elective-rec-tool-64c5bddd4ed3.herokuapp.com/

# Setup Instructions

# Prerequisites    
- Python 3.x
- NO DEPENDENCIES

# Installation
Clone the project repository to your local machine:

      git clone https://github.com/yourusername/csce-elective-recommendation-tool.git
      cd csce-elective-recommendation-tool

Directory Structure
    
    data/
    ├── tracked_elective_list.txt  # List of electives grouped by track
    └── course_catalog.txt         # Catalog with descriptions and prerequisites
    static/
    ├── popup.css                  # stylesheet for course description popup
    ├── search.css                 # stylesheet for main page
    templates/
    ├── popup.html                 # html file for for course description popup
    ├── search.html                # html file for for main page
    bm25.py                        # BM25 algorithm logic
    data.py                        # Data cleaning functions for electives and catalog
    main.py                        # Script to execute BM25 query and output recommendations
    
# Running the Code Locally
Prepare the Data
    Ensure the elective list (tracked_elective_list.txt) and course catalog (course_catalog.txt) files are in the data/ directory.

Execute the Script
    From the root directory, run the following command:   
    python3 main.py
    Open search.html with live server.
    
      
   When prompted to list your interests separated by commas, enter a comma-separated list of your interests and press the submit button.

    Ex. "software engineering, web design, python"
    
   The website will display the classes ranked under each track, with the top 7 tracks as corresponding with both interests and requirements highlighted in green.
