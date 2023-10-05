register = document.querySelector('.register')
login = document.querySelector('.login')
post = document.querySelector('.post_tag')

registerAlert = document.querySelector('.register-alert')
loginAlert = document.querySelector('.login-alert')
postAlert = document.querySelector('.post-alert')

if (register) {
    if (registerAlert.classList.contains('hidden')) {
        registerAlert.classList.remove('hidden')
    }
}

if (login) {
    if (loginAlert.classList.contains('hidden')) {
        loginAlert.classList.remove('hidden')
    }
}

if (post) {
    if (postAlert.classList.contains('hidden')) {
        postAlert.classList.remove('hidden')
    }
}

function resetErrors() {
    if (!registerAlert.classList.contains('hidden')) {
        registerAlert.classList.add('hidden')
    }
    if (!loginAlert.classList.contains('hidden')) {
        loginAlert.classList.add('hidden')
    }
    if (!postAlert.classList.contains('hidden')) {
        postAlert.classList.add('hidden')
    }
}