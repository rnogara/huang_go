let contactBtn = document.getElementById('contact-btn');
let scheduleBtn = document.getElementById('schedule-btn');
let contactForm = document.getElementsByClassName('contact-form');

contactBtn.addEventListener('click', toggleHide(contactBtn));
scheduleBtn.addEventListener('click', toggleHide(scheduleBtn));

contactForm.addEventListener('submit', emailSender(contactForm));

function toggleHide(e) {
    e.preventDefault();
    e.classList.add('hide');
    if (e.id === 'contact-btn') {
        document.getElementsByClassName('contact').classList.remove('hide');
    }
    if (e.id === 'schedule-btn') {
        document.getElementsByClassName('schedule').classList.remove('hide');
    }
}

function emailSender(e) {
    e.preventDefault();
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;
    let data = {
        title: 'Contato do site',
        name: name,
        email: email,
        message: message
    }
}

