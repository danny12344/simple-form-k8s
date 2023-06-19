function handleSubmit(event) {
  event.preventDefault(); // Prevents the default form submission
  
  // Get the form values
  var name = document.getElementById("name").value;
  var password = document.getElementById("password").value;
  
  // Display the form contents in the div element
  var formResultsDiv = document.getElementById("formResults");
  formResultsDiv.textContent = "Name: " + name + "<br>" + "Password: " + password;
}
