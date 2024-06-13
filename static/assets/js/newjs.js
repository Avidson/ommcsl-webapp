

/** code to process image uploaded via form**/
 var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
  };


  /* code for validation of passcode */

document.querySelector('.pin-input').addEventListener('input', validateInput);
function validateInput(e) {
  const el = e.target;
  if (el.validity.patternMismatch) {
    el.value = el.value.slice(0, -1);
    return false;
  }
  return true;
};

/* Password validation */

function validate_password() {
 
  var pass = document.getElementById('pass').value;
  var confirm_pass = document.getElementById('re-pass').value;
  document.getElementById('create-account-submit').disabled = true;
  if (pass != confirm_pass) {
      document.getElementById('wrong_pass_alert').style.color = 'red';
      document.getElementById('wrong_pass_alert').innerHTML= '☒ Use same pin';
      document.getElementById('create-account-submit').disabled = true;
      document.getElementById('create-account-submit').style.opacity = (0.4);
  } else {
      document.getElementById('wrong_pass_alert').style.color = 'green';
      document.getElementById('wrong_pass_alert').innerHTML =
          '🗹 Pin Matched';
      document.getElementById('create-account-submit').disabled = false;
      document.getElementById('create-account-submit').style.opacity = (1);
  }
};

function wrong_pass_alert() {
  if (document.getElementById('pass').value != "" &&
      document.getElementById('re-pass').value != "") {
      alert("Your response is submitted");
  } else {
      alert("Please fill all the fields");
  }
};


/*  */