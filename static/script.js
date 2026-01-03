function send() {
  const input = document.getElementById("input");
  const messages = document.getElementById("messages");

  let text = input.value.trim().toLowerCase();
  if (text === "") return;

  // Message utilisateur
  messages.innerHTML += `<div class="user">👤 ${input.value}</div>`;
  input.value = "";

  let reply = "";

  // ===== SALUTATIONS =====
  if (
    text.includes("salut") ||
    text.includes("bonjour") ||
    text.includes("salam")
  ) {
    reply = "👋 Salut Cheikh, je suis là. Tu veux parler rap, wolof ou projets ?";
  }

  // ===== IDENTITÉ =====
  else if (
    text.includes("qui es tu") ||
    text.includes("c'est qui") ||
    text.includes("tu es quoi")
  ) {
    reply = "🤖 Je suis ton assistant personnel, créé par Cheikh Diallo.";
  }

  // ===== RAP =====
  else if (
    text.includes("rap") ||
    text.includes("rapper") ||
    text.includes("texte")
  ) {
    reply =
      "🎤 Le rap c’est la vérité.\nÉcris ce que tu vis.\nVeux-tu un texte rap en wolof ou en français ?";
  }

  // ===== WOLOF =====
  else if (
    text.includes("wolof") ||
    text.includes("wollof") ||
    text.includes("langue")
  ) {
    reply =
      "🗣️ Wolof bi mooy sunu racine.\nWax ak xel, wax ak doole.\nTu veux un texte street ou conscient ?";
  }

  // ===== AIDE =====
  else if (
    text.includes("aide") ||
    text.includes("aider") ||
    text.includes("help")
  ) {
    reply =
      "🧠 Je peux t’aider pour :\n- écrire du rap\n- améliorer ton wolof\n- créer des idées\nDis-moi ce que tu veux.";
  }

  // ===== INCONNU =====
  else {
    reply =
      "🤔 Je n’ai pas encore compris.\nEssaie : rap, wolof, aide, salut.";
  }

  // Message bot
  messages.innerHTML += `<div class="bot">🤖 ${reply}</div>`;

  // Scroll automatique
  messages.scrollTop = messages.scrollHeight;
}
