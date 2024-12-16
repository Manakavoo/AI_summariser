// Authentication Handling
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            await handleLogin(event);
        });
    }

    if (signupForm) {
        signupForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            await handleSignup(event);
        });
    }
});

async function handleLogin(event) {
    const form = event.target;
    const email = form.querySelector('input[name="email"]').value;
    // const password = form.querySelector('input