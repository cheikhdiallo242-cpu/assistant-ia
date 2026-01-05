import random

# Mémoire simple (conversation)
MEMORY = []

# =========================
# TEXTES RAP CONSCIENT WOLOF
# =========================
RAP_WOLOF_CONSCIENT = [
    "Xel bu leer mooy doole gu dëgg, ku xam sa bopp du jaay sa xol.",
    "Rap bi du mbubb, mooy xam-xam buy daw ci micro.",
    "Nit ku gëm ay ndox, man dama gëm ay wax.",
    "Street du safara, ignorance mooy safara.",
    "Dëgg du metti, waaye déglu dëgg mooy liggéey.",
    "Sama plume dafay jooy, waaye sama wax dafay faj.",
    "Rap conscient du yëngal xel yi, du yëngal ego.",
    "Ku dul xam fu mu joge, du xam fu mu dem.",
    "Xol bu dëgër, xel bu leer, mooy sama armure.",
    "Baat bi mooy arme, silence mooy poison.",
    "Nit ñi di daw vérité, man dama koy top.",
    "Rap du ay baat rekk, mooy responsabilité.",
    "Ku am xel du ragal baat.",
    "Dëgg mooy sama chemin, rap mooy sama guide.",
    "Sama rap du néw, dafay réveiller.",
]

# =========================
# FONCTION POUR FAIRE UN COUPLET
# =========================
def make_verse(lines=6):
    lines = min(lines, len(RAP_WOLOF_CONSCIENT))
    selected = random.sample(RAP_WOLOF_CONSCIENT, lines)
    return "🎤 COUPLET :\n" + "\n".join(selected)

# =========================
# CERVEAU PRINCIPAL
# =========================
def generate_response(messages):
    user_text = messages[-1]["content"].lower()
    MEMORY.append(user_text)

    # Salutations
    if "salut" in user_text or "slt" in user_text or "bonjour" in user_text:
        return "👋 Salut Cheikh. Tu veux du rap conscient, freestyle ou wolof pur ?"

    # Rap conscient wolof
    if "conscient" in user_text and "wolof" in user_text:
        return make_verse(6)

    # Rap conscient
    if "conscient" in user_text:
        return make_verse(5)

    # Freestyle
    if "freestyle" in user_text:
        return make_verse(7)

    # Rap général
    if "rap" in user_text:
        return "🎤 Dis-moi : conscient, freestyle ou wolof."

    # Mémoire (illusion d’intelligence)
    if len(MEMORY) >= 4:
        return "🧠 Je te suis. Continue, ton message est clair."

    # Réponse par défaut
    return "🤔 Reformule un peu. Je suis là pour créer avec toi."
