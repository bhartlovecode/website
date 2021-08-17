idBox = document.getElementById("id");
idBox.addEventListener("click",function(){
    let inputID = idBox.value;
    if(inputID === "123456"){
        fillFields();
    }
});

//Function to fill fields upon id entry
function fillFields(){
    console.log(document.cookie);
    let deleteFirstCookie = document.cookie.replace('valid=true; ', "");
    let splitOne = deleteFirstCookie.split("=");
    console.log(splitOne);
    let splitTwo = splitOne[1].split(",");
    console.log(splitTwo);
    //Parses out the values from cookie
    for(let i = 0; i < splitTwo.length; i++){
        let values = splitTwo[i].toString().split(":");
        if(values.length > 2){ //Used to fix inputted website while retaining ':' as separator
            let valuesAfter = [values[1], values[2]];
            let str = valuesAfter.join(":");
            let el = document.getElementById(values[0]);
            el.value = str;

        }

        else if(values[1] === "true"){//button or box
            document.getElementById(values[0]).checked = true;
        }

        else if (values[1] === "false"){
            document.getElementById(values[0]).checked = false;
        }


        else{
            let el = document.getElementById(values[0]);
            el.value = values[1];
        }

    }


}

/*This function validates the registration options
Custom error is displayed upon invalid submission
Redirected to "thankyou.html" if valid*/
function onSubmit() {
    document.getElementById("fields").action = "";
    document.cookie = "valid=" + 'false' + ";max-age=" + 60*60*24*365;
    //This gathers all of the selections (radio buttons and checkboxes)
    let eachSelection = [];
    let x = 0;

    let selections = document.getElementsByClassName("selection");
    for (let i = 0; i < selections.length; i++) {
        if (selections[i].checked) {
            eachSelection[x] = selections[i];
            x++;
        }
    }

    //If there are any selections
    if (eachSelection.length > 0) {
        //If room1_B is selected for session one and another workshop is chosen in session two
        if (eachSelection[0].value === "Room_1B" && eachSelection.length > 2) {

            //Grabs the dimensions for centering
            let leftOffset = (screen.width - 500) / 2;
            let topOffset = (screen.height - 400) / 4;
            let secondSelection = eachSelection[1].value;

            //Creates a popup window and centers it in the screen
            let popupWindow = window.open("", null, "height=400 width=500" +
                ",left=" + leftOffset + ", top=" + topOffset);

            //Custom message depending on selections causing error
            popupWindow.document.write('<!DOCTYPE html><html lang="en" id = "errorDisplay"><head><title>Registration Error</title></head>');
            popupWindow.document.write('<body id = "err_body"><h1 id ="err_header">Error!</h1><p>Workshop Two of Java Development encompasses ' +
                'the entire Day. Your selection ' + secondSelection + ' for Python Development is not valid!</p></body>');

            //This styles the popup window to have different css than the standard document
            popupWindow.document.getElementById("err_header").style.color = "white";
            popupWindow.document.getElementById("err_body").style.background = "black";
            popupWindow.document.getElementById("err_body").style.color = "green";
            popupWindow.document.getElementById("errorDisplay").style.fontSize = 'x-large';
            popupWindow.document.getElementById("errorDisplay").style.textAlign = 'center';
            popupWindow.document.write('<link href="../css/webdefault.css" rel="stylesheet" type="text/css"/>');
           popupWindow.document.close();
        }

        //If Building Snake and Python and How to Use Rules are not chosen together (one or the either is picked alone)
        else if ((eachSelection[1].value === "Room_1C" && eachSelection[2].value !== "Room_1B") ||
        eachSelection[2].value === "Room_1B" && eachSelection[1].value !== "Room_1C")  {

            //Grabs the dimensions for centering
            let leftOffset = (screen.width - 500) / 2;
            let topOffset = (screen.height - 400) / 4;
            let secondSelection = eachSelection[1].value;
            let thirdSelection = eachSelection[2].value;

            //Creates a popup window and centers it in the screen
            let popupWindow = window.open("", null, "height=400 width=500" +
                ",left=" + leftOffset + ", top=" + topOffset);

            //Custom message depending on selections causing the error
            popupWindow.document.write('<!DOCTYPE html><html lang="en" id = "errorDisplay"><head><title>Registration Error</title></head>');
            popupWindow.document.write('<body id = "err_body"><h1 id ="err_header">Error!</h1><p>Building Snake in ' +
                'Python and How to Use Rules MUST be taken in conjunction. Your selections of ' + secondSelection +
        ' for Python Development and ' + thirdSelection + ' for Writing in Prolog are not valid.</p></body>');

            //This styles the popup window to have different css than the standard document
            popupWindow.document.getElementById("err_header").style.color = "white";
            popupWindow.document.getElementById("err_body").style.background = "black";
            popupWindow.document.getElementById("err_body").style.color = "green";
            popupWindow.document.getElementById("errorDisplay").style.fontSize = 'x-large';
            popupWindow.document.getElementById("errorDisplay").style.textAlign = 'center';
            popupWindow.document.write('<link href="../css/webdefault.css" rel="stylesheet" type="text/css"/>');
            popupWindow.document.close();
        }

        //If the choices are valid, redirect to thankyou.html
            //Captures all elements for usage in cookie
        else{
            let title = document.getElementById("title").value
            let firstName = document.getElementById("firstName").value;
            let lastName = document.getElementById("lastName").value;
            let addressOne = document.getElementById("addressOne").value;
            let addressTwo = document.getElementById("addressTwo").value;
            let city = document.getElementById("city").value;
            let state = document.getElementById("state").value;
            let zipCode = document.getElementById("zipCode").value;
            let number = document.getElementById("number").value;
            let email = document.getElementById("email").value;
            let website = document.getElementById("website").value;
            let position = document.getElementById("position").value;
            let compName = document.getElementById("compName").value;
            let mealPack = document.getElementById("meal_pack").checked;
            let dinner_day_two = document.getElementById("dinner_day_2").checked;
            let java_one = document.getElementById("java_one").checked;
            let java_two = document.getElementById("java_two").checked;
            let java_three = document.getElementById("java_three").checked;
            let python_checkbox_one = document.getElementById("python_checkbox_one").checked;
            let python_checkbox_two = document.getElementById("python_checkbox_two").checked;
            let python_checkbox_three = document.getElementById("python_checkbox_three").checked;
            let prolog_one = document.getElementById("prolog_one").checked;
            let prolog_two = document.getElementById("prolog_two").checked;
            let prolog_three = document.getElementById("prolog_three").checked;
            let billing_first_name = document.getElementById("billing_first_name").value;
            let billing_last_name = document.getElementById("billing_last_name").value;
            let visa = document.getElementById("visa").checked;
            let mastercard = document.getElementById("mastercard").checked;
            let american_express = document.getElementById("american_express").checked;
            let card_number = document.getElementById("card_number").value;
            let csv = document.getElementById("csv").value;
            let exp_year = document.getElementById("exp_year").value;
            let exp_month = document.getElementById("exp_month").value;

            let cookieValue = "title:"+title+",firstName:"+firstName+",lastName:"+lastName+",addressOne:"+addressOne+
            ",addressTwo:"+addressTwo+",city:"+city+",state:"+state+",zipCode:"+zipCode+",number:"+number+
            ",email:"+email+",website:"+website+",position:"+position+",compName:"+compName+",meal_pack:"+mealPack+
                ",dinner_day_2:"+dinner_day_two+
                ",java_one:"+java_one+",java_two:"+java_two+",java_three:"+java_three+
                ",python_checkbox_one:"+python_checkbox_one+",python_checkbox_two:"+python_checkbox_two+
            ",python_checkbox_three:"+python_checkbox_three+",prolog_one:"+prolog_one+",prolog_two:"+prolog_two+
                ",prolog_three:"+prolog_three+",billing_first_name:"+billing_first_name+
            ",billing_last_name:"+billing_last_name+",visa:"+visa+",mastercard:"+mastercard+
                ",american_express:"+american_express+",card_number:"+card_number+
                ",csv:"+csv+",exp_year:"+exp_year+",exp_month:"+exp_month+";path:/";
            document.cookie = "123456=" + cookieValue + ";max-age=" + 60*60*24*365;
            document.cookie = "valid=" + 'true' + ";max-age=" + 60*60*24*365;
        }
    }



}

//This function verifies that only one checkbox is checked at any given time
function checkBoxValidation(){
    let numOfChecks = [document.getElementById("python_checkbox_one"),
    document.getElementById("python_checkbox_two"), document.getElementById("python_checkbox_three")];
    let counter = 0;
    for(let i = 0; i < numOfChecks.length; i++){
        if(numOfChecks[i].checked === true){
            counter++;
        }

        if(counter > 1){
            counter--;
            numOfChecks[i].checked = false;
        }
    }
}

