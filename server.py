"""
Principal module du fichier server
"""

# Modules tiers
from flask import render_template
import connexion


# Création de l'instance de l'application
app = connexion.App(__name__, specification_dir="./")

# Lecture du fichier swagger.yml pour configurer les points d'arrivée
app.add_api("swagger.yml")


# Création d'une URL pour "/"
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port=8080,debug=True)
