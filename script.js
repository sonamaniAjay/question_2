document.getElementById('login-form').addEventListener('submit', ()=> {
    const userId = document.getElementById('userId').value;
    const password = document.getElementById('password').value;
    
    if (userId && password) {
        alert('User login successful!');
    } else {
        alert('Please fill all the fields!');
    }
});
function submitOnEnter(event) {
    if (event.key === "Enter") {
        event.preventDefault();  
        document.getElementById("login-form").submit();  
    }
}