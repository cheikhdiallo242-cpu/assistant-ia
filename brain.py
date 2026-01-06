import random

memory = {}

# ====== BANQUES DE PHRASES ======

INTRO_WOLOF = [
    "Xel bu leer, xol bu dëgër",
    "Dund bi dafa metti waaye jàng la",
    "Sama wax du ay fenn",
    "Rap du poésii rekk, mooy dund",
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
    "🎶 Dëgg laay wax, du ma fenn",
]

INTRO_FR = [
    "J’écris pour les miens",
    "La rue m’a tout appris",
    "Ce rap vient du cœur",
]

LINES_FR = [
    "La vérité dérange mais elle libère",
    "J’avance seul mais droit",
    "Le succès sans valeurs ne vaut rien",
    "Chaque cicatrice raconte une histoire",
    "Je rappe pour survivre pas pour plaire",
]

REFRAIN_FR = [
    "🎶 Rap conscient, parole sincère",
    "🎶 Même dans l’ombre je reste clair",
]

SALUTATIONS = ["salut", "bonjour", "slt", "hello", "salam"]

# ====== GÉNÉRATION ======

def generate_verse(lines, n=5):
    return random.sample(lines, n)

def generate_rap(language):
    if language == "wolof":
        verse1 = generate_verse(LINES_WOLOF, 5)
        refrain = random.sample(REFRAIN_WOLOF, 2)
        verse2 = generate_verse(LINES_WOLOF, 5)

        return (
            "🎤 " + random.choice(INTRO_WOLOF) + "\n\n"
            + "\n".join(verse1) + "\n\n"
            + "\n".join(refrain) + "\n\n"
            + "\n".join(verse2)
        )

    if language == "fr":
        verse1 = generate_verse(LINES_FR, 5)
        refrain = random.sample(REFRAIN_FR, 2)
        verse2 = generate_verse(LINES_FR, 5)

        return (
            "🎤 " + random.choice(INTRO_FR) + "\n\n"
            + "\n".join(verse1) + "\n\n"
            + "\n".join(refrain) + "\n\n"
            + "\n".join(verse2)
        )

    return "Choisis une langue."

# ====== CERVEAU ======

def think(user_id, message):
    msg = message.lower().strip()

    if user_id not in memory:
        memory[user_id] = {
            "language": None
        }

    if any(w in msg for w in SALUTATIONS):
        return "👋 Salut Cheikh. Wolof ou Français ?"

    if "qui t'a créé" in msg or "qui t’a créé" in msg:
        return "🤖 J’ai été créé par Cheikh Diallo pour le rap conscient."

    if "wolof" in msg:
        memory[user_id]["language"] = "wolof"
        return "🗣️ Wolof activé. Dis *conscient* ou écris un thème."

    if "français" in msg or "francais" in msg:
        memory[user_id]["language"] = "fr"
        return "🇫🇷 Français activé. Dis *conscient* ou écris un thème."

    if msg in ["encore", "autre", "continue"]:
        return generate_rap(memory[user_id]["language"])

    if len(msg.split()) > 6:
        return generate_rap(memory[user_id]["language"])

    if "conscient" in msg:
        return generate_rap(memory[user_id]["language"])

    return "🎤 Dis *encore*, *autre*, ou écris un thème."
