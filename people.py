"""
Ceci est le module people module où sont définies toutes les actions ReST pour la collection
PEOPLE
"""

# Module système
from datetime import datetime

# Modules tiers
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Données utilisées par l'API
PEOPLE = {
            "Dupont": {
                    "fname": "Jean",
                    "lname": "Dupont",
                    "timestamp": get_timestamp()
            },
            "Durand": {                
                    "fname": "Louise",
                    "lname": "Durand",
                    "timestamp": get_timestamp()
            },
            "Lopez": {
                    "fname": "François",
                    "lname": "Lopez",
                    "timestamp": get_timestamp()
            } 
}


def read_all():
    # Création d'une liste à partir des données
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    # La personne est-elle enregistrée dans people?
    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    # sinon, message
    else:
        abort(
            404, "La personne de nom de famille {lname} n'a pas été trouvée".format(lname=lname)
        )

    return person


def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # La personne est-elle déjà enregistrée ?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )

    # Sinon, elle est enregistrée -> message d'erreur
    else:
        abort(
            406,
            "La personne de nom de famille {lname} est déjà enregistrée".format(lname=lname),
        )


def update(lname, person):
    # La personne est-elle enregistrée dans people ?
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]

    # sinon, message d'erreur
    else:
        abort(
            404, "La personne de nom de famille {lname} n'a pas été trouvée".format(lname=lname)
        )


def delete(lname):
    # La personne est-elle enregistrée dans people ?
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Sinon, message d'erreur
    else:
        abort(
            404, "La personne de nom de famille {lname} n'a pas été trouvée".format(lname=lname)
        )
