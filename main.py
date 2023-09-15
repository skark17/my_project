from classifications import main, classify
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def webpage():
    if request.method == "POST":
        cc = request.form.get("cc")
        cs = request.form.get("cs")
        csur = request.form.get("csur")
        b = request.form.get("b")
        h = request.form.get("h")

        capColor = int(cc)
        capShape = int(cs)
        capSurface = int(csur)
        bruises = int(b)
        habitat = int(h)

        userSelection = main(capColor, capShape, capSurface, bruises, habitat)
        message = classify(userSelection)
        return message
    return render_template("webpage.html")


if __name__ == '__main__':
    app.run()