# test encode decode jwt
import base64
import jwt
import json

import base64

# read private key from disk
private_key = open('./keys/jwt-key-aedes-hackaton').read()
pub_key = open('./keys/jwt-key-aedes-hackaton.pub').read()

data = {
        "jti": "beb7879ae80b2045830862784f7e1a69",
        "iat": 1614847438,
        "nbf": 1614847438,
        "exp": 1614847468,
        "iss": "https://api.acc2.mijn.overheid.nl/delen/gegevens",
        "aud": "woonnetrijnmond",
        "sub": "98abe733-4e3a-4d5b-8ed8-6202d7cf9a57",
        "brp": {
          "voornamen": "Hugo",
          "voorvoegselGeslachtsnaam": "",
          "geslachtsnaam": "Koopmans",
          "voorvoegselPartnernaam": "",
          "partnernaam": "",
          "huisnummer": "14",
          "huisletter": "",
          "huisnummerToevoeging": "",
          "huisnummerAanduiding": "by",
          "postcode": "6626AB",
          "geboortedatum": "19690922"
        },
        "bri": {
          "inkomens": {
            "2019": {
              "inkomen": 63000,
              "grondslag": "1000001",
              "status": "1000019"
            },
            "2020": {
              "inkomen": 65000,
              "grondslag": "1000001",
              "status": "1000019"
            }
          }
        },
        "verklaring": {
          "tekst": "De persoon waarvan de gegevens in dit bericht zijn opgenomen, heeft ingelogd bij MijnOverheid en toestemming gegeven om de gegevens uit dit bericht te delen met de genoemde ontvanger (aud)",
          "authenticatiedienst": "digid",
          "betrouwbaarheidsniveau": "substantieel",
          "tijdstempelAuthenticatie": 1614847422
        }
      }

token = jwt.encode(data,private_key,algorithm="RS256")

print(token)

padded = token + "=="
bytedata = base64.urlsafe_b64decode(padded)
jsondata = bytedata.decode('utf-8',errors='ignore')
#print(jsondata)

#decoded = jwt.decode(token,pub_key,algorithms="RS256")


#print(decoded)
