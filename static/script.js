var form = document.getElementById("form");
var formName = document.getElementById("formname");
var description = document.getElementById("description");
var myQuestion = document.getElementById("myQuestion");
var question = document.getElementById("question");
var inputType = document.getElementById("inputType");
var list = document.getElementById("List")
var formContainer =document.getElementById("form_container")
var data = {}
var screeninfo = []
let form_info = {
    form: "",
    form_description: "",
    screen_info: screeninfo,
}

form.addEventListener("submit",(e=>{
    e.preventDefault();
    form_info['form']=formName.value;
    form_info['form_description']=description.value;
    return form_info;
}
))

myQuestion.addEventListener("submit", (e) => {
    e.preventDefault();
    var data = {
        question: question.value,
        input: inputType.value,
        useroption: list.value
    };
    addToList(data);
    data=createForm({
        form: formName.value,
        form_description: description.value,
        screen_info: screeninfo
    });
    form_info = data
    
    // Clear input fields
    question.value = "";
    inputType.value = "";
    list.value = "";
});
function addToList(data) {
    screeninfo.push(data)
    return screeninfo
}
//Form Generator

function createForm(data) {
    var formContainer = document.getElementById('form_container');
    formContainer.innerHTML = "";
    const form_title = data['form']
    const title = document.getElementById('form_title')
    title.textContent = form_title

    for (let i in data.screen_info) {
        if (data.screen_info[i]['input'] == "Text") {
            var input = document.createElement('input');
            input.type = data.screen_info[i]['input'];
        } else if (data.screen_info[i]['input'] == "Textarea") {
            var input = document.createElement('textarea');
            input.type = data.screen_info[i]['input'];
        } else if (data.screen_info[i]['input'] == "Radiobutton") {
            let radiogrp = document.createElement('div')
            const optionList = data.screen_info[i]['useroption'].split(',');
            var list = optionList.forEach((value, index) => {
                //creating label element
                let label = document.createElement('label')
                label.textContent = value;
                //creating an input element of type radio
                let radio = document.createElement('input');
                radio.type = "radio";
                radio.name = "optionList";
                radio.value = value;
                radiogrp.appendChild(radio)
                radiogrp.appendChild(label)
                //radiogrp.appendChild(document.createElement('br'));
            })
            var input = radiogrp;
        } else if (data.screen_info[i]['input'] == "dropdown") {
            let select = document.createElement('select');
            const optionList = data.screen_info[i]['useroption'].split(',');
            optionList.forEach((value, index) => {
                let option = document.createElement('option');
                option.value = value;
                option.textContent = value;
                select.appendChild(option);
            });
            var input = select;

        }
        if (input) {
            // Create the label for the current input field
            const label = document.createElement('label');
            label.textContent = data.screen_info[i]['question'];


            // Check and log input and label before appending
            //console.log('Appending label:', label);
            //console.log('Appending input:', input);

            // Append label, input, and line breaks to the form container
            formContainer.appendChild(label);
            //formContainer.appendChild(document.createElement('br'));
            formContainer.appendChild(input);
            formContainer.appendChild(document.createElement('br'));

        } else {
            console.error("Invalid input type for element:", screenInfo['input']);
        }
       
    }
    const button = document.createElement('button');
    button.textContent = "Save Form"
    button.type = "submit"
    formContainer.appendChild(button)
    return data;
}
formContainer.addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent default form submission
    e.stopPropagation(); // Stop event propagation to parent elements
    sendData(form_info);
});


function sendData(data) {
    console.log(data);
    data = JSON.stringify(data);

    // Send POST request to Flask server
    fetch("http://localhost:1601/4", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",  // Ensure JSON is sent correctly
        },
        body: data,
    })
    .then(response => response.json())
    .then(data => {
        // Handle server response here
        console.log("Server response:", data);
    })
    .catch(error => {
        console.error("Error sending data:", error);
    });
}
