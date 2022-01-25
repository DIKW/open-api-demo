import connexion
from flask import abort
import six

from swagger_server.models.huishouden import Huishouden  # noqa: E501
from swagger_server.models.toets_resultaat_lokale_binding import ToetsResultaatLokaleBinding  # noqa: E501
from swagger_server.models.toets_resultaat_met_kale_huur import ToetsResultaatMetKaleHuur  # noqa: E501
from swagger_server.models.toets_resultaat_segmenten import ToetsResultaatSegmenten  # noqa: E501
from swagger_server.models.woonduren_inner import WoondurenInner  # noqa: E501
from swagger_server import util
# hk add inkomen model
from swagger_server.models.inkomen_bri import InkomenBri  # noqa: F401,E501
from swagger_server.models.inkomen_brp import InkomenBrp  # noqa: F401,E501
from swagger_server.models.inkomen_verklaring import InkomenVerklaring  # noqa: F401,E501
from swagger_server.models.inkomen import Inkomen  # noqa: E501
from typing import List, Dict  # noqa: F401
# hk
import jwt
import json
from datetime import datetime
import cryptography


# read private key from disk
private_key = open('./keys/jwt-key-aedes-hackaton').read()
pub_key = open('./keys/jwt-key-aedes-hackaton.pub').read()
dvmg_key = open('./keys/dvgm.pub').read()

def aedes_verhuurtoets_lokale_bindings_toets_post(body):  # noqa: E501
    """Toetst woonduur volgens lokaal geldende toetsingskader

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: ToetsResultaatLokaleBinding
    """
    # parameters
    parameters = {
                "drempelwaardewoonduur":   48}

    
    if connexion.request.is_json:
        body = [WoondurenInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

        maxwoonduur = max({x.woonduur: x for x in body})
        
        prsn = []
        for x in body:
            payload = {"voornamen": x.voornamen,
                       "voorvoegselGeslachtsnaam": x.voorvoegsel_geslachtsnaam,
                       "geslachtsnaam": x.geslachtsnaam,
                       "woonduur": x.woonduur}
            prsn.append(payload)
            

    toets = ToetsResultaatLokaleBinding()

    toets.toets_resultaat_lokale_binding = maxwoonduur >= parameters["drempelwaardewoonduur"]
    toets.personen = prsn

    toets.jwt = jwt.encode({'data' : {'personen' : prsn, 
                                      'toets_resultaat_lokale_binding' : str(toets.toets_resultaat_lokale_binding)}},
                                       private_key, 
                                       algorithm="RS256")

    #toets.jwt = jwt.encode(json.dumps(payload), "my_certificaat", algorithm="HS256")

    return toets


def aedes_verhuurtoets_passendheidstoets_bri_met_kale_huur_post(body):  # noqa: E501
    """Toetst kale huur volgens het geldende nationale toetsingskader

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ToetsResultaatMetKaleHuur
    """
    # parameters
    parameters = {
                "index2019":   1.0523,
                "index2020":   1.0248,
                "aowLeeftijd": 796,
                "lageAftoppingsgrens": 633.25,
                "hogeAftoppingsgrens": 678.66,
                "igEenPersoonsNietAow":  23725,
                "igEenPersoonsWelAow":   23650,
                "igMeerPersoonsNietAow": 32200,
                "igMeerPersoonsWelAow":  32075
                }

    if connexion.request.is_json:
        body = Huishouden.from_dict(connexion.request.get_json())  # noqa: E501
        # als inkomens_ondertekend gevuld dan gebruik deze

        # is er jwt data aanwezig?
        if len(body.inkomens_ondertekend) > 0 :
            if(body.controleer_handtekening):
                # we kiezen voor de jwt encrypted inkomens
                # TODO: pak uit en verifieer handtekening
                try :
                    inkomens = [jwt.decode(i,pub_key,algorithms="RS256") for i in body.inkomens_ondertekend]
                except jwt.exceptions.ExpiredSignatureError:
                    return {"msg":"Signature expired"}, 401
                except jwt.exceptions.InvalidKeyError:
                    return {"msg":"Not a valid key"}, 401
            else:
                # we controleren niet
                inkomens = [jwt.decode(i,options={"verify_signature": False}) for i in body.inkomens_ondertekend]
        else:
                # geen ondertekende inkomens beschikbaar dus gaan er van uit dat inkoms is gevuld
            if(len(body.inkomens)>0):
                # gebruik inkomens as is
                inkomens = body.inkomens
            else:
                # STOP geen inkomen gegevens
                return {"msg":"geen valide inkomens data ontvangen"}, 206

        # aantal personen in huishouden
        aantalPersonen = len(inkomens) + body._aantal_meeverhuizende_kinderen

        # aow leeftijd in maanden
        lftd = 0
        now = datetime.today()
        gbds = []
        gezinsInks = 0.0
        # personen voor in de response
        prsn = []
        for ink_dict in inkomens:
            # map decoded dict into object model
            ink = Inkomen.from_dict(ink_dict)

            gbd = datetime.strptime(ink.brp.geboortedatum, '%Y%m%d')
            gbds.append((now.year - gbd.year) * 12 + (now.month - gbd.month))
            gezinsInks =+ ink.bri.inkomens._2019.inkomen * parameters["index2019"] + ink.bri.inkomens._2020.inkomen * parameters["index2020"]
        
            payload = {"voornamen": ink.brp.voornamen,
                       "voorvoegselGeslachtsnaam": ink.brp.voorvoegsel_geslachtsnaam,
                       "geslachtsnaam": ink.brp.geslachtsnaam}
            prsn.append(payload)
        

        isAOWHuishouden = (max(gbds) > parameters["aowLeeftijd"])

        # tabel passend toewijzen
        toets = ToetsResultaatMetKaleHuur()

        # map personen
        toets.personen = prsn
        
        isDrieOfMeer = aantalPersonen > 2
        isTweePers = aantalPersonen == 2
        isEenPers = aantalPersonen == 1
        
        # hoge grens
        passend_tot_hoge_aftoppingsgrens = (isDrieOfMeer and not(isAOWHuishouden) and gezinsInks < parameters["igMeerPersoonsNietAow"]) or \
            (isDrieOfMeer and isAOWHuishouden and gezinsInks < parameters["igMeerPersoonsNietAow"] )

        # lage grens
        passend_tot_lage_aftoppingsgrens = (passend_tot_hoge_aftoppingsgrens) or \
            (isEenPers and not(isAOWHuishouden) and gezinsInks < parameters["igEenPersoonsNietAow"]) or \
            (isTweePers and not(isAOWHuishouden) and gezinsInks < parameters["igMeerPersoonsNietAow"]) or \
            (isEenPers and isAOWHuishouden and gezinsInks < parameters["igEenPersoonsAow"]) or \
            (isTweePers and isAOWHuishouden and gezinsInks < parameters["igMeerPersoonsAow"]) 


        toets.toets_resultaat = False

        if (body._kale_huur >= parameters["lageAftoppingsgrens"] and body._kale_huur < parameters["hogeAftoppingsgrens"]) :
            toets.toets_resultaat = passend_tot_hoge_aftoppingsgrens

        if (body._kale_huur < parameters["lageAftoppingsgrens"]) :
            toets.toets_resultaat = passend_tot_lage_aftoppingsgrens

    return toets


def aedes_verhuurtoets_passendheidstoets_bri_segmenten_post(body):  # noqa: E501
    """Toetst verhuursegmenten van huurder(s) volgens het geldende nationale toetsingskader

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ToetsResultaatSegmenten
    """
    # parameters
    parameters = {
                "index2019":   1.0523,
                "index2020":   1.0248,
                "aowLeeftijd": 796,
                "lageAftoppingsgrens": 633.25,
                "hogeAftoppingsgrens": 678.66,
                "igEenPersoonsNietAow":  23725,
                "igEenPersoonsWelAow":   23650,
                "igMeerPersoonsNietAow": 32200,
                "igMeerPersoonsWelAow":  32075
                }

    if connexion.request.is_json:
        body = Huishouden.from_dict(connexion.request.get_json())  # noqa: E501
        
        # is er jwt data aanwezig?
        if len(body.inkomens_ondertekend) > 0 :
            if(body.controleer_handtekening):
                # we kiezen voor de jwt encrypted inkomens
                # TODO: pak uit en verifieer handtekening
                try :
                    inkomens = [jwt.decode(i,pub_key,algorithms="RS256") for i in body.inkomens_ondertekend]
                except jwt.exceptions.ExpiredSignatureError:
                    return {"msg":"Signature expired"}, 401
                except jwt.exceptions.InvalidKeyError:
                    return {"msg":"Not a valid key"}, 401
            else:
                # we controleren niet
                inkomens = [jwt.decode(i,options={"verify_signature": False}) for i in body.inkomens_ondertekend]
        else:
                # geen ondertekende inkomens beschikbaar dus gaan er van uit dat inkoms is gevuld
            if(len(body.inkomens)>0):
                # gebruik inkomens as is
                inkomens = body.inkomens
            else:
                # STOP geen inkomen gegevens
                return {"msg":"geen valide inkomens data ontvangen"}, 206



        # aantal personen in huishouden
        aantalPersonen = len(body.inkomens) + body._aantal_meeverhuizende_kinderen

        # aow leeftijd in maanden
        lftd = 0
        now = datetime.today()
        gbds = []
        # personen voor in response
        prsn = []
        gezinsInks = 0.0
        for ink in body.inkomens:
            gbd = datetime.strptime(ink.brp.geboortedatum, '%Y%m%d')
            gbds.append((now.year - gbd.year) * 12 + (now.month - gbd.month))
            gezinsInks =+ ink.bri.inkomens._2019.inkomen * parameters["index2019"] + ink.bri.inkomens._2020.inkomen * parameters["index2020"]
        
            payload = {"voornamen": ink.brp.voornamen,
                "voorvoegselGeslachtsnaam": ink.brp.voorvoegsel_geslachtsnaam,
                "geslachtsnaam": ink.brp.geslachtsnaam}
            prsn.append(payload)

        isAOWHuishouden = (max(gbds) > parameters["aowLeeftijd"])

        # tabel passend toewijzen
        toets = ToetsResultaatSegmenten()
        
        # map personen
        toets.personen = prsn
                
        isDrieOfMeer = aantalPersonen > 2
        isTweePers = aantalPersonen == 2
        isEenPers = aantalPersonen == 1
        
        # hoge grens
        toets.toets_resultaat_tot_hoge_aftoppingsgrens = (isDrieOfMeer and not(isAOWHuishouden) and gezinsInks < parameters["igMeerPersoonsNietAow"]) or \
            (isDrieOfMeer and isAOWHuishouden and gezinsInks < parameters["igMeerPersoonsNietAow"] )

        toets.toets_resultaat_tot_lage_aftoppingsgrens = (toets.toets_resultaat_tot_hoge_aftoppingsgrens) or \
            (isEenPers and not(isAOWHuishouden) and gezinsInks < parameters["igEenPersoonsNietAow"]) or \
            (isTweePers and not(isAOWHuishouden) and gezinsInks < parameters["igMeerPersoonsNietAow"]) or \
            (isEenPers and isAOWHuishouden and gezinsInks < parameters["igEenPersoonsAow"]) or \
            (isTweePers and isAOWHuishouden and gezinsInks < parameters["igMeerPersoonsAow"]) 


    return toets
