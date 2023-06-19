function handleSubmit(event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const password = document.getElementById("password").value;

  fetch("/submit", {
    method: "POST",
    body: new URLSearchParams({
      name: name,
      password: password
    })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("formResults").innerText = data.message;
    });
}
