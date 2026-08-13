/* Yomin Electric — shared product page behavior: theme, nav, gallery, WeChat */
(function () {
  // Theme
  var storedTheme = localStorage.getItem('ym_theme');
  var hour = new Date().getHours();
  var autoTheme = (hour >= 6 && hour < 18) ? 'light' : 'dark';
  var isLight = (storedTheme || autoTheme) === 'light';
  function setTheme(light) {
    document.body.classList.toggle('light', light);
    var b = document.querySelectorAll('.theme-btn-s');
    if (b.length >= 2) { b[0].classList.toggle('active', !light); b[1].classList.toggle('active', light); }
  }
  setTheme(isLight);
  var btnD = document.getElementById('btnDark');
  var btnL = document.getElementById('btnLight');
  if (btnD) btnD.addEventListener('click', function () { setTheme(false); localStorage.setItem('ym_theme', 'dark'); });
  if (btnL) btnL.addEventListener('click', function () { setTheme(true); localStorage.setItem('ym_theme', 'light'); });

  // Nav scroll
  var nav = document.getElementById('nav');
  if (nav) window.addEventListener('scroll', function () { nav.classList.toggle('sc', window.scrollY > 40); });

  // Mobile menu
  var ham = document.getElementById('ham');
  var mob = document.getElementById('mob');
  var mobX = document.getElementById('mob-x');
  if (ham && mob) ham.addEventListener('click', function () { mob.classList.toggle('op'); });
  if (mobX && mob) mobX.addEventListener('click', function () { mob.classList.remove('op'); });

  // Gallery thumbnails
  var mainImg = document.getElementById('mainImg');
  if (mainImg) {
    document.querySelectorAll('.g-thumbs img').forEach(function (t) {
      t.addEventListener('click', function () {
        mainImg.src = t.getAttribute('data-full');
        mainImg.alt = t.getAttribute('alt');
        document.querySelectorAll('.g-thumbs img').forEach(function (o) { o.classList.remove('active'); });
        t.classList.add('active');
      });
    });
  }

  // WeChat modal
  var wcBtn = document.getElementById('wc-btn');
  var wcClose = document.getElementById('wc-close');
  var wcOverlay = document.getElementById('wc-overlay');
  if (wcBtn && wcOverlay) wcBtn.addEventListener('click', function () { wcOverlay.classList.add('op'); });
  if (wcClose && wcOverlay) wcClose.addEventListener('click', function () { wcOverlay.classList.remove('op'); });
  if (wcOverlay) wcOverlay.addEventListener('click', function (e) { if (e.target === e.currentTarget) e.currentTarget.classList.remove('op'); });
})();
