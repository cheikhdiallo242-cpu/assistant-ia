import random

memory = {}

SALUTATIONS = ["salut", "bonjour", "slt", "hello", "salam"]
POSITIVE = ["nice", "cool", "bien", "lourd", "fort"]
THEME_WORDS = ["thème", "theme", "écris un thème", "ecris un theme"]

INTRO_WOLOF = [
    "Xel bu leer, xol bu dëgër",
    "Dund bi dafa metti waaye jàng la",
    "Rap du ay fenn",
    "Sama wax mooy dund",
]

LINES_WOLOF = [
    "Nit ku xam sa bopp du topp mbubb mi",
    "Ku muñ moo gën a dox",
    "Dëgg du am xarit waaye mooy ndam",
    "Xel bu rafet mooy alal bu gëna rëy",
    "Sama baat dafay taxaw, du daw",
    "Yoon wi gudd na waaye ndam neex na",
    "Rap conscient du mbëggeel ak fitna",
    "Ku ragal Yàlla du ñakk yoon",
]

REFRAIN_WOLOF = [
    "🎶 Xel bu leer, xol bu dëgër",
    "🎶 Rap bi mooy sama liggéey",
]

def generate_rap(theme=None):
    verse1 = random.sample(LINES_WOLOF, 5)
    verse2 = random.sample(LINES_WOLOF, 5)
    refrain = random.sample(REFRAIN_WOLOF, 2)

    theme_line = f"🎯 Thème : {theme}\n\n" if theme else ""

    return (
        f"🎤 {random.choice(INTRO_WOLOF)}\n\n"
        + theme_line
        + "\n".join(verse1) + "\n\n"
        + "\n".join(refrain) + "\n\n"
        + "\n".join(verse2)
    )

def think(user_id, message):
    msg = message.lower().strip()

    if user_id not in memory:
        memory[user_id] = {
            "language": None,
            "awaiting_theme": False
        }

    # SALUT
    if any(w in msg for w in SALUTATIONS):
        return "👋 Salut Cheikh. Tu veux du rap en wolof ou français ?"

    # QUI T'A CRÉÉ
    if "qui t'a créé" in msg or "qui t’a créé" in msg:
        return "🤖 J’ai été créé par Cheikh Diallo pour le rap conscient."

    # FEEDBACK POSITIF
    if any(w in msg for w in POSITIVE):
        return "🔥 Content que ça te plaise. On est ensemble 💪"

    # CHOIX LANGUE
    if "wolof" in msg:
        memory[user_id]["language"] = "wolof"
        return "🗣️ Wolof activé. Dis *conscient* ou donne un thème."

    # DEMANDE DE THÈME
    if any(w in msg for w in THEME_WORDS):
        memory[user_id]["awaiting_theme"] = True
        return "🎯 OK. Donne-moi un thème (ex : rue, foi, amour, succès)."

    # RÉCEPTION DU THÈME
    if memory[user_id]["awaiting_theme"]:
        memory[user_id]["awaiting_theme"] = False
        return generate_rap(theme=message)

    # ENCORE / AUTRE
    if msg in ["encore", "autre", "continue"]:
        return generate_rap()

    # CONSCIENT
    if "conscient" in msg:
        return generate_rap()

    return "🎤 Dis *encore*, *écris un thème*, ou donne un sujet."
