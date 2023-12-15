function initUpdateBtns() {
    
    let btns = document.getElementsByClassName('btn')
    let contactBox = document.getElementByClassName('contact-box')
    let scheduleBox = document.getElementByClassName('schedule-box')

    for (i = 0; i < btns.length; i++) {
        btns[i].addEventListener('click', function(){
            this.classList.toggle('hide');
            if (this.id === 'contact-btn') {
                contactBox.classList.toggle('hide');
            }
            if (this.id === 'schedule-btn') {
                scheduleBox.classList.toggle('hide');
            }
        })
    }
}

document.addEventListener('DOMContentLoaded', initUpdateBtns)