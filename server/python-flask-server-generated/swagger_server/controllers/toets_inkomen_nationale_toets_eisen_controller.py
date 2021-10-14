import connexion
import six

from swagger_server.models.huishouden import Huishouden  # noqa: E501
from swagger_server.models.toets_resultaat import ToetsResultaat  # noqa: E501
from swagger_server import util

# hk
from datetime import datetime


def huurder_nationale_inkomenstoets_post(body):  # noqa: E501
    """Toetst inkomen van huurder volgens de geldende nationale toetsingskader

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ToetsResultaat
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
        # aantal personen in huishouden
        aantalPersonen = len(body.inkomens) + body._aantal_meeverhuizende_kinderen

        # aow leeftijd in maanden
        lftd = 0
        now = datetime.today()
        gbds = []
        gezinsInks = 0.0
        for ink in body.inkomens:
            gbd = datetime.strptime(ink.brp.geboortedatum, '%Y%m%d')
            gbds.append((now.year - gbd.year) * 12 + (now.month - gbd.month))
            gezinsInks =+ ink.bri.inkomens._2019.inkomen * parameters["index2019"] + ink.bri.inkomens._2020.inkomen * parameters["index2020"]
        
        isAOWHuishouden = (max(gbds) > parameters["aowLeeftijd"])

        # tabel passend toewijzen
        toets = ToetsResultaat()
        
        isDrieOfMeer = aantalPersonen > 2
        isTweePers = aantalPersonen == 2
        isEenPers = aantalPersonen == 1
        
        # hoge grens
        toets.passend_tot_hoge_aftoppingsgrens = (isDrieOfMeer and not(isAOWHuishouden) and gezinsInks < parameters["igMeerPersoonsNietAow"]) or \
            (isDrieOfMeer and isAOWHuishouden and gezinsInks < parameters["igMeerPersoonsNietAow"] )

        toets.passend_tot_lage_aftoppingsgrens = (toets.passend_tot_hoge_aftoppingsgrens) or \
            (isEenPers and not(isAOWHuishouden) and gezinsInks < parameters["igEenPersoonsNietAow"]) or \
            (isTweePers and not(isAOWHuishouden) and gezinsInks < parameters["igMeerPersoonsNietAow"]) or \
            (isEenPers and isAOWHuishouden and gezinsInks < parameters["igEenPersoonsAow"]) or \
            (isTweePers and isAOWHuishouden and gezinsInks < parameters["igMeerPersoonsAow"]) 


        toets.passend = False

        if (body._kale_huur >= parameters["lageAftoppingsgrens"] and body._kale_huur < parameters["hogeAftoppingsgrens"]) :
            toets.passend = toets.passend_tot_hoge_aftoppingsgrens

        if (body._kale_huur < parameters["lageAftoppingsgrens"]) :
            toets.passend = toets.passend_tot_lage_aftoppingsgrens

    return toets
