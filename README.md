# Very Simple Static Site Generator with DevServer
- Runs on python
- requires beautifulsoup and few packages for navigation and other features

# Usage
## Setup Environment
- mkvirtualenv manang
- pip install -r requirements.txt

## Run
- python devserver.py

## Configuration
- See src/README.md for the workflow details  

## Static Assets
- Simply keep in the root folder 
- eg. 
 * src/pages
 * src/pagelets
 * build/...
 * assets/js/
 * assets/css/
 * assets/images/ , etc ...
- The assets are accessed as assets/images/file.jpg , so on
