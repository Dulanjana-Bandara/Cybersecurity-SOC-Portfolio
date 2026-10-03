const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav-links');

toggle?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(open));
});

document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => nav.classList.remove('open'));
});

const labs = document.getElementById('allLabs');
const labsBtn = document.getElementById('toggleLabs');

labsBtn?.addEventListener('click', () => {
  const collapsed = labs.classList.toggle('collapsed');
  labsBtn.textContent = collapsed ? 'Show all labs' : 'Show less';
});

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

const sections = [...document.querySelectorAll('.section-anchor')];
const links = [...document.querySelectorAll('.nav-links a[href^="#"]')];

function updateActiveNav() {
  const y = window.scrollY + 140;
  let active = '';
  sections.forEach(section => {
    if (y >= section.offsetTop) active = section.id;
  });
  links.forEach(link => {
    link.classList.toggle('active', link.getAttribute('href') === `#${active}`);
  });
}

const topBtn = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
  updateActiveNav();
  topBtn?.classList.toggle('show', window.scrollY > 650);
}, { passive: true });

topBtn?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

const tiltCard = document.getElementById('tiltCard');
if (tiltCard && window.matchMedia('(pointer:fine)').matches) {
  tiltCard.addEventListener('mousemove', e => {
    const r = tiltCard.getBoundingClientRect();
    const x = e.clientX - r.left;
    const y = e.clientY - r.top;
    const rx = ((y / r.height) - 0.5) * -6;
    const ry = ((x / r.width) - 0.5) * 7;
    tiltCard.style.transform = `perspective(1200px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-2px)`;
  });
  tiltCard.addEventListener('mouseleave', () => {
    tiltCard.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg)';
  });
}

document.getElementById('year').textContent = new Date().getFullYear();
updateActiveNav();
