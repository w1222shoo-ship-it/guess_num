let gameId = null;
const history = [];

function setStatus(text){ document.getElementById('status').textContent = text }

function updateAttempts(n){ document.getElementById('attempts').textContent = `嘗試次數: ${n}` }

function addHistory(item){
  history.unshift(item);
  const ul = document.getElementById('history');
  const li = document.createElement('li');
  li.textContent = item;
  ul.prepend(li);
}

function enableGame(enabled){
  document.getElementById('guessInput').disabled = !enabled;
  document.getElementById('guessBtn').disabled = !enabled;
}

async function startGame(){
  const resp = await fetch('/start', { method: 'POST' });
  const j = await resp.json();
  gameId = j.game_id;
  setStatus('遊戲開始！請輸入猜測。');
  updateAttempts(0);
  document.getElementById('result').textContent = '';
  document.getElementById('startBtn').textContent = '重新開始';
  enableGame(true);
}

async function sendGuess(){
  if (!gameId){ setStatus('請先按「開始遊戲」'); return; }
  const input = document.getElementById('guessInput');
  const value = input.value;
  if (!value){ setStatus('請輸入數字'); return; }

  const resp = await fetch('/guess', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ game_id: gameId, guess: value })
  });
  const j = await resp.json();
  if (j.error){ setStatus(j.error); return; }

  updateAttempts(j.attempts);
  addHistory(`第 ${j.attempts} 次：你猜 ${value} → ${j.result}`);

  const resEl = document.getElementById('result');
  resEl.className = 'result';
  if (j.result === 'too_big'){
    resEl.textContent = '太大'; resEl.classList.add('warn');
  } else if (j.result === 'too_small'){
    resEl.textContent = '太小'; resEl.classList.add('warn');
  } else if (j.result === 'correct'){
    resEl.textContent = `恭喜！共猜了 ${j.attempts} 次`;
    resEl.classList.add('success');
    enableGame(false);
  }

  input.value = '';
  input.focus();
}

document.getElementById('startBtn').addEventListener('click', startGame);
document.getElementById('guessBtn').addEventListener('click', sendGuess);

document.getElementById('guessInput').addEventListener('keydown', function(e){
  if (e.key === 'Enter') sendGuess();
});

// initialize
enableGame(false);
