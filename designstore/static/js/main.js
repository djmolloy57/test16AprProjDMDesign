var form = document.getElementById('form')

form.addEventListener('submit',function(event){ //if doesnt work submit Continue for submit
  event.preventDefault() // prevents the form from autosubmitting

  var name_str = document.getElementById('name').value
  console.log("Name: " + name_str)

  var email_str = document.getElementById('email').value
  console.log("Email: " + email_str)

  var design_type = document.getElementById('type').value
  console.log("Design Type: " + design_type)

  var size_str = document.getElementById('size').value
  console.log("Size: " + size_str)

  var desc_str = document.getElementById('description').value
  console.log("Description: " + desc_str)


})