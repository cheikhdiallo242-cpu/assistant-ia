# brain.py

# Mémoire simple par utilisateur
memory = {}

def think(user_id, message):
    text = message.lower().strip()

    # Initialiser la mémoire utilisateur
    if user_id not in memory:
        memory[user_id] = {
            "lang": None,
            "mode": None
        }

    user = memory[user_id]

    # ===== SALUT / BONJOUR =====
    if any(word in text for word in ["salut", "bonjour", "slt", "hello", "hi"]):
        return (
            "👋 Salut Cheikh.\n"
            "Je suis ton assistant IA personnel.\n"
            "Tu veux du rap, du freestyle, ou une discussion consciente ?"
        )

    # ===== QUI T'A CRÉÉ =====
    if "qui t'a créé" in text or "qui ta créé" in text or "qui es tu" in text:
        return (
            "🤖 J’ai été créé par Cheikh.\n"
            "Un esprit créatif qui aime le rap conscient,\n"
            "le wolof, la vérité et la réflexion.\n"
            "Je suis là pour l’aider à s’exprimer."
        )

    # ===== LANGUE =====
    if "wolof" in text:
        user["lang"] = "wolof"
        return "🗣️ Wolof noté. Tu veux du rap conscient ou du freestyle ?"

    if "français" in text or "francais" in text:
        user["lang"] = "fr"
        return "🇫🇷 Français noté. Rap conscient ou freestyle ?"

    # ===== MODE =====
    if "conscient" in text:
        user["mode"] = "conscient"
        return generate_rap(user["lang"], "conscient")

    if "freestyle" in text:
        user["mode"] = "freestyle"
        return generate_rap(user["lang"], "freestyle")

    # ===== PAR DÉFAUT =====
    return (
        "🤔 Je n’ai pas bien compris.\n"
        "Dis par exemple : wolof, français, conscient ou freestyle."
    )


def generate_rap(lang, mode):
    if lang == "wolof" and mode == "conscient":
        return (
            "🎤 Xel bu leer, xol bu dëgër, dund gu am solo.\n"
            "Nit ku xam sa bopp du topp mbubb mi.\n"
            "Aduna du ay xaalis rekk, mooy ay jikko.\n"
            "Rap bi sama jamono, wax ju dëgg laay yónni.\n"
            "Dund bi metti, waaye sax dama taxaw."
        )

    if lang == "wolof" and mode == "freestyle":
        return (
            "🔥 Wax ma dal, sama flow dafa raw.\n"
            "Mic bi ci sama loxo, sama xel dafay daw.\n"
            "Street bi sama école, dund bi sama beat.\n"
            "Freestyle bu am doole, bu dul fen."
        )

    if lang == "fr" and mode == "conscient":
        return (
            "🎤 J’écris pour comprendre, pas pour briller.\n"
            "Le rap c’est la vérité quand le monde ment.\n"
            "Chaque mot est un pas vers la lumière.\n"
            "Je rappe pour ceux qu’on n’écoute jamais."
        )

    if lang == "fr" and mode == "freestyle":
        return (
            "🔥 Freestyle en feu, j’improvise sans filet.\n"
            "Les mots coulent comme la nuit sur la ville.\n"
            "Pas besoin de refrain quand le flow parle."
        )

    return "🤖 Choisis une langue et un style."
