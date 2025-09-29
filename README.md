This is an app created by the Gemini CLI on Google Cloud (with a little input and troubleshooting on my part). To run it, do the following:

* Log into https://console.cloud.google.com

* Get a Gemini API key here: https://aistudio.google.com/app/api-keys
  * Create a new project
  * Create a new key for your project
  * Add your api key to the end of your .bashrc file with
    * `nano ~/.bashrc`
    * Add this line: `export GOOGLE_API_KEY="<key>"` where "key" is the API key you just created
    * This will save it for future sessions, but you'll either need to log out and back in again or run that line of code from the command prompt (i.e. export GEMINI_API_KEY="<key>")

* Set up your python virtual environment
  * `python -m venv .venv` (this only needs to be run once)
  * `source .venv/bin/activate` (this will need to be run each time you restart your terminal)
  * `pip install streamlit google-genai` (this only needs to be run once)

* Clone the repository and set up the app (only needs to be run once)
  * `git clone https://github.com/johnsonra/recipeApp`
  * `cd recipeApp`
  * `pip install -r requirements.txt`

* Start the app
  * `streamlit run app.py --server.port=8080 --server.address=0.0.0.0 --server.enableCORS=false`
