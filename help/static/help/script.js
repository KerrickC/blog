function validation(){
    var name = document.getElementById("name").value;
    var subject = document.getElementById("subject").value;
    var phone = document.getElementById("phone").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;
    var error_message = document.getElementById("error_message");
    var errtxt;

    error_message.style.padding = "10px";

    if(name.length < 2){
        text = "Please enter a valid name."
        error_message.innerHTML = text;
        return false;
    }
    if(subject.length < 1){
        text = "Please enter a valid subject."
        error_message.innerHTML = text;
        return false;
    }
    if(isNaN(phone) || phone.length != 10){
        text = "Please enter a valid phone number."
        error_message.innerHTML = text;
        return false;
    }
    if(email.indexOf("@")==-1 || email.length < 6){
        text = "Please enter a valid email."
        error_message.innerHTML = text;
        return false;
    }
    if(message.length <= 20){
        text = "Please enter more than 20 characters."
        error_message.innerHTML = text;
        return false;
    }


    alert("Form sumbitted successfully!")

    return false;

}