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

THEMES = {
    "rue": [
        "Rue bi dafa jàngal, du école",
        "Ku am doole ci rue am xel",
        "Bitim-réew du yomb waaye moo may doole",
        "Rue bi mooy sama livre bu jëkk",
        "Ci trottoir la ma jàng dund",
    ],
    "foi": [
        "Ku ragal Yàlla du ñakk yoon",
        "Ñaan mooy sama arme",
        "Dëgg ak muus mooy sama guide",
        "Yàlla rekk mooy sama soutien",
        "Xol bu leer di wut ndimbal",
    ],
    "amour": [
        "Mbëggeel du ay wax rekk",
        "Xol bu gën a metti mooy bu bëgg",
        "Amour dafay may doole ak metit",
        "Ku bëgg dëgg, bëgg metit",
        "Mbëggeel mooy jangoro bu neex",
    ],
}

REFRAIN_WOLOF = [
    "🎶 Xel bu leer, xol bu dëgër",
    "🎶 Rap bi mooy sama liggéey",
]

def generate_rap(theme=None):
    if theme and theme.lower() in THEMES:
        base_lines = THEMES[theme.lower()]
    else:
        base_lines = LINES_WOLOF

    couplet1 = random.sample(base_lines, min(5, len(base_lines)))
    couplet2 = random.sample(base_lines, min(5, len(base_lines)))
    refrain = random.sample(REFRAIN_WOLOF, 2)

    return (
        f"🎤 {random.choice(INTRO_WOLOF)}\n"
        f"🎯 Thème : {theme}\n\n"
        + "\n".join(couplet1)
        + "\n\n🎶 " + " / ".join(refrain) + " 🎶\n\n"
        + "\n".join(couplet2)
        + "\n\n🎶 " + " / ".join(refrain) + " 🎶"
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
