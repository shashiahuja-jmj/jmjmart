from flask import Flask, render_template

app = Flask(__name__)

categories = [
    {
        "name": "EV Chargers",
        "image": "https://images.unsplash.com/photo-1593941707882-a5bac6861d75?q=80&w=1200"
    },
    {
        "name": "Smart Security",
        "image": "https://images.unsplash.com/photo-1558002038-1055907df827?q=80&w=1200"
    },
    {
        "name": "Solar Products",
        "image": "https://images.unsplash.com/photo-1509391366360-2e959784a276?q=80&w=1200"
    },
    {
        "name": "Networking",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        categories=categories
    )

if __name__ == "__main__":
    app.run(debug=True)
	if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)