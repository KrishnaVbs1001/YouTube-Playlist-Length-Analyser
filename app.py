from flask import Flask, render_template, url_for, request
from analyzer import get_playlist_id, analyze

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        playlist_link = request.form.get('playlist_link').strip()
        playlist_id = get_playlist_id(playlist_link)
        duration, no_of_videos, popular_videos, ttle = analyze(playlist_id)
        
        data = [duration, no_of_videos, popular_videos, ttle]
        return render_template("home.html", data=data)
    else:
        return render_template("home.html")

@app.errorhandler(Exception)
def handle_error(error):
    return render_template("error.html", error=error)


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
