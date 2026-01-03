function send() {
  const input = document.getElementById("input");
  const messages = document.getElementById("messages");

  const userText = input.value.trim();
  if (!userText) return;

  const text = userText.toLowerCase();

  messages.innerHTML += `<div class="user">👤 ${userText}</div>`;
  input.value = "";

  let reply = "🤖 Je réfléchis... reformule ta question.";

  // ====== BASE DE TEXTES RAP ======
  const rapTexts = [
    "🎤 Je rappe pour sortir du noir, xel bu leer, cœur solide dans le brouillard.",
    "🎤 Micro en main, vérité dans la voix, dakar la nuit, je parle pour les miens.",
    "🎤 Pas besoin d’or pour briller, j’ai la parole et la dalle.",
    "🎤 Wolof dans la tête, le rap dans les veines, je trace ma route sans haine.",
    "🎤 Ils parlent trop, moi j’écris vrai, vécu gravé, flow affûté."
  ];

  // ====== RÉPONSES CONDITIONNELLES ======
  if (text.includes("salut") || text.includes("bonjour")) {
    reply = "👋 Salut Cheikh, comment je peux t’aider ?";
  }
  else if (text.includes("qui es tu")) {
    reply = "🤖 Je suis ton assistant personnel, créé par Cheikh.";
  }
  else if (text.includes("wolof")) {
    reply = "🗣️ Wolof bi mooy racine bi. Wax ak xel, wax ak doole.";
  }
  else if (
    text.includes("rap") ||
    text.includes("texte") ||
    text.includes("freestyle")
  ) {
    const randomIndex = Math.floor(Math.random() * rapTexts.length);
    reply = rapTexts[randomIndex];
  }
  else if (text.includes("aide")) {
    reply = "🧠 Je peux t’aider à écrire du rap, améliorer ton wolof et créer des idées.";
  }

  messages.innerHTML += `<div class="bot">${reply}</div>`;
}
