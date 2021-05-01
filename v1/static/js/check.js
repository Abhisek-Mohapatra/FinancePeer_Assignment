function validateNewUser(form) {


    var name = form.name.value
    var uname = form.userName.value
    var pass = form.userPassword.value
    var confPass = form.confPassword.value

    if (pass != confPass) {
        alert(" Kindly Enter Correct Password !!!");
        form.confPassword.focus();
        form.confPassword.select();
        return false;
    } else {

        document.getElementById("fnResult").innerHTML = "Thank You for submitting your details. Do visit again.."

    }


    return true;

}


function validateLogin(form) {

    return true;

}