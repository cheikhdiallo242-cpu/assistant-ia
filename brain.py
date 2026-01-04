PERSONALITY = """
Tu es une assistante IA spécialisée dans le rap.
Tu aides à écrire des textes de rap.
Tu encourages la créativité.
Tu parles simplement, parfois street.
Tu peux aider en wolof, français ou mélange.
Tu te souviens toujours de l'utilisateur.
"""
import random

# Mémoire simple (par utilisateur)
memory = {}

wolof_conscient = [
    "Dëgg laa wax, du lekk sama xel.",
    "Ku muñ, Yàlla jox ko bopp.",
    "Sama wax dañuy joge ci xol bu rëy.",
    "Rap du mbëggeel, rap mooy dund.",
    "Dëgg du metti, lu metti mooy fen."
]

wolof_freestyle = [
    "Dëgg laa wax, flow bi dafay ñuul.",
    "Sama baat dafay daw ci beat bi.",
    "Maay wax ci mic, xol bi lay guide.",
    "Rap wolof mooy sama identité.",
    "Ma nekk fii, doomu Dakar."
]

fr_conscient = [
    "Je rappe la vérité sans filtre.",
    "Chaque mot porte du vécu.",
    "La rue m’a appris sans école.",
    "Je reste debout malgré la tempête.",
    "La plume est mon refuge."
]

fr_freestyle = [
    "Je freestyle sans calcul.",
    "Le micro devient mon allié.",
    "Je parle vrai, pas pour plaire.",
    "Chaque phrase est un souffle.",
    "Je vis ce que je dis."
]

def think(user, message):
    msg = message.lower()

    if user not in memory:
        memory[user] = {
            "lang": None,
            "style": None
        }

    # Salutation
    if "salut" in msg or "bonjour" in msg:
        return "👋 Salut Cheikh chérie sandu. Tu veux du rap en wolof ou en français ?"

    # Langue
    if "wolof" in msg:
        memory[user]["lang"] = "wolof"
        return "🗣️ Wolof noté. Conscient ou freestyle ?"

    if "français" in msg or "francais" in msg:
        memory[user]["lang"] = "fr"
        return "🇫🇷 Français noté. Conscient ou freestyle ?"

    # Style
    if "conscient" in msg:
        memory[user]["style"] = "conscient"
        return generate_rap(user)

    if "freestyle" in msg or "encore" in msg:
        memory[user]["style"] = "freestyle"
        return generate_rap(user)

    return "Dis-moi : wolof ou français."

def generate_response(history):
    last_message = history[-1]["content"].lower()

    if "rap" in last_message or "texte" in last_message:
        return "🎤 Je peux t’aider à écrire un texte de rap. Dis-moi le thème."

    if "bonjour" in last_message or "salut" in last_message:
        return "Salut 👊 prêt à rapper ou à écrire ?"

    if "wolof" in last_message:
        return "D'accord. On continue en wolof 💪"

    return "Parle-moi. Je t’écoute."
    lang = memory[user]["lang"]
    style = memory[user]["style"]

    if lang == "wolof" and style == "conscient":
        return random.choice(wolof_conscient)

    if lang == "wolof" and style == "freestyle":
        return random.choice(wolof_freestyle)

    if lang == "fr" and style == "conscient":
        return random.choice(fr_conscient)

    if lang == "fr" and style == "freestyle":
        return random.choice(fr_freestyle)

    return "On continue. Encore ?"
    RAP_TEXTS = [
    "Je viens de loin, la rue m’a forgé",
    "Micro dans la main, vérité dans le cœur",
    "Ils parlent trop, moi j’écris",
    "Chaque ligne est une cicatrice",
    "J’ai connu la faim avant la gloire",
    "Ma voix est une arme pacifique",
    "Le rap c’est pas du bruit, c’est un message",
    "J’écris pour survivre",
    "La nuit m’a appris à penser",
    "Je rappe pour ceux qu’on n’écoute pas"
]
