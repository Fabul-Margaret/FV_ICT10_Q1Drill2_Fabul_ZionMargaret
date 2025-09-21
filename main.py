from pyscript import document, display

def generate_message(*args, **kwargs):  #had to use "*args, **kwargs" to avoid error bcs if I don't the site wouldn't generate the message pls check docs file for my citation
    # assign strings to variables
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # use escape characters and concatenation
    msg = "\t(●'◡'●)STUDENT PROFILE\n"
    msg += "Name: " + name + "\n"
    msg += "Age: " + age + "\n"
    msg += "School: " + school + " \n"
    msg += "--------------------------------\n"
    msg += "\tNotes!\n"
    msg += name + " is currently " + age + " years old and studies at " + school + ".\n"
    msg += "This information that you are reading was gathered through input fields and displayed a multiline string in Python via PyScript🤑💅" + ".\n"

    # clear previous and display new message
    document.getElementById("output").innerText = "" 
    document.getElementById("output").innerText = msg
