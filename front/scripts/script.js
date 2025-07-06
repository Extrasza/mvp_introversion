document.getElementById('avaliacao-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const dados = {
    Time_spent_Alone: parseFloat(document.getElementById('tempo_sozinho').value),
    Stage_fear: document.getElementById('medo_palco').value === 'true',
    Social_event_attendance: parseFloat(document.getElementById('eventos_sociais').value),
    Going_outside: parseFloat(document.getElementById('saidas').value),
    Drained_after_socializing: document.getElementById('cansaco_social').value === 'true',
    Friends_circle_size: parseFloat(document.getElementById('amigos').value),
    Post_frequency: parseFloat(document.getElementById('postagens').value)
  };

  try {
    const resposta = await fetch('http://127.0.0.1:5000/personalidade', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(dados)
    });

    if (!resposta.ok) {
      throw new Error(`Erro ao chamar API: ${resposta.status}`);
    }

    const json = await resposta.json();
    alert("O resultado foi: " + json.resultado);
  } catch (error) {
    alert("Erro ao enviar a avaliação: " + error.message);
    console.error(error);
  }
});