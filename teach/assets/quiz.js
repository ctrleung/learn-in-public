/* Reusable quiz component.
   Usage: <div id="quiz"></div> plus <script type="application/json" id="quiz-data">
   [{"q":"...","options":["a","b","c"],"answer":1,"why":"...","cite":"<a href=...>...</a>"}]
   Then <script src="../assets/quiz.js"></script>. Gives instant feedback per question and a final score. */
(function () {
  var root = document.getElementById('quiz'), raw = document.getElementById('quiz-data');
  if (!root || !raw) return;
  var items = JSON.parse(raw.textContent), done = 0, correct = 0;
  var score = document.createElement('p'); score.className = 'score';
  items.forEach(function (it, n) {
    var box = document.createElement('div'); box.className = 'q';
    var p = document.createElement('p'); p.textContent = (n + 1) + '. ' + it.q; box.appendChild(p);
    var fb = document.createElement('div'); fb.className = 'fb'; fb.setAttribute('aria-live', 'polite');
    var btns = it.options.map(function (text, i) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'opt'; b.textContent = text;
      b.addEventListener('click', function () {
        btns.forEach(function (x) { x.disabled = true; });
        var ok = i === it.answer;
        b.classList.add(ok ? 'right' : 'wrong');
        if (!ok) btns[it.answer].classList.add('right');
        fb.className = 'fb ' + (ok ? 'ok' : 'no');
        fb.innerHTML = (ok ? 'Correct. ' : 'Not quite. ') + it.why + (it.cite ? ' <span class="cite">' + it.cite + '</span>' : '');
        done++; if (ok) correct++;
        if (done === items.length) score.textContent = 'Score: ' + correct + ' / ' + items.length + '. Come back in a few days and try again from memory.';
      });
      box.appendChild(b); return b;
    });
    box.appendChild(fb); root.appendChild(box);
  });
  root.appendChild(score);
})();
