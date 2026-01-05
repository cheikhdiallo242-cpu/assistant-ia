import random

# 🧠 Mémoire simple par utilisateur
memory = {}

# 🎤 BANQUE DE TEXTES RAP CONSCIENT (Wolof)
RAP_CONSCIENT_WOLOF = [
    "Xel bu leer, xol bu dëgër, dund gu am solo.",
    "Dëgg la rap, du mbubb, du fén, du dolo.",
    "Sama wax dafay daw, moo raw doole ak xaalis.",
    "Ku am xel du jaay sa bopp, du jaay sa taalif.",
    "Nopp naa aduna, gis naa fenkat yi bari.",
    "Rap bi di yoon, di taalibe, di ndigël ci bari.",

    "Nit ku xam sa bopp du topp mbubb mi.",
    "Xel mu fees ak leer mooy arme bi gën.",
    "Dund bi dafa metti waaye sax du war a dem.",
    "Sama wax dafay jëme ci ndam, du jëme ci wem.",

    "Rap conscient du mbëggeel rekk, mooy jangoro.",
    "Wax dëgg mooy def xol yi am ndox.",
    "Lu ñu bëgg a dégg du lu ñu war a wax.",
    "Waaye rappeur bu dëgg du ragal benn wax."
]

# 🎤 RAP FRANÇAIS CONSCIENT
RAP_FR = [
    "J’écris pour réveiller les cerveaux endormis.",
    "La vérité dérange, voilà pourquoi elle est bannie.",
    "J’ai vu trop de rêves mourir dans le silence.",
    "Alors je rappe pour donner un sens à l’existence."
]

def generate_response(user_id, message):
    msg = message.lower()

    # Initialiser mémoire utilisateur
    if user_id not in memory:
        memory[user_id] = {
            "langue": "wolof",
            "style": "conscient"
        }

    # Détection langue / style
    if "wolof" in msg:
        memory[user_id]["langue"] = "wolof"
    if "français" in msg or "francais" in msg:
        memory[user_id]["langue"] = "fr"
    if "conscient" in msg:
        memory[user_id]["style"] = "conscient"

    # 🎯 GÉNÉRATION MULTI-PHRASES
    lines = []

    if memory[user_id]["langue"] == "wolof":
        lines = random.sample(RAP_CONSCIENT_WOLOF, 5)
    else:
        lines = random.sample(RAP_FR, 4)

    # 🔥 IMPORTANT : joindre les lignes
    return "\n".join(lines)
