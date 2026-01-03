function send() {
  const input = document.getElementById("input");
  const messages = document.getElementById("messages");

  const text = input.value.toLowerCase();
  if (!text) return;

  messages.innerHTML += `<div>👤 ${input.value}</div>`;
  input.value = "";

  let reply = "Je réfléchis... reformule ta question.";

  if (text.includes("salut") || text.includes("bonjour")) {
    reply = "👋 Salut Cheikh, comment je peux t’aider ?";
  } else if (text.includes("rap")) {
    reply = "🎤 Le rap c’est la vérité : écris vrai, vis vrai, rappe vrai.";
  } else if (text.includes("wolof")) {
    reply = "🗣️ Wolof bi mooy racine bi. Wax ak xel, wax ak doole.";
  } else if (text.includes("ciel")) {
    reply = "🌤️ Le ciel est bleu à cause de la diffusion de la lumière du soleil.";
  } else if (text.includes("qui es tu")) {
    reply = "🤖 Je suis ton assistant personnel, créé par Cheikh.";
  }

  messages.innerHTML += `<div>🤖 ${reply}</div>`;
}
