
var form = document.getElementById("form");
var formName = document.getElementById("formname");
var description = document.getElementById("description");
var myQuestion =document.getElementById("myQuestion");
var question = document.getElementById("question");
var inputType = document.getElementById("inputType");
var list = document.getElementById("List")
var screeninfo = []
const form_info = {
    form : "",
    form_description: "",
    screen_info : "",
}
form.addEventListener("submit", (e => {
    e.preventDefault();
    let screendata = [] ;
    const form_info = {
        form : formName.value,
        form_description : description.value,
        screen_info : screendata
    }
    /*console.log(form_info);*/
    myQuestion.addEventListener("submit",(e=>{
        e.preventDefault();
        var data = {
            question : question.value,
            input : inputType.value,
            useroption: list.value
        }
        
        screendata = addToList(data)
        console.log(screendata)
        form_info['screen_info'] = screendata,
        console.log(form_info)
    })) 
}))
function addToList(data){
    screeninfo.push(data)
    return screeninfo
}



