//Creates and submits a hidden form that aims to delete a selected library item.
function deleteItem(id, item_type) 
{
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/admin/delete_item');
    form.style.display = 'hidden';
    var id_field = document.createElement("input");
    var item_type_field = document.createElement("input");
    id_field.type = "hidden";
    id_field.value = id;
    id_field.name = "id";
    item_type_field.type = "hidden";
    item_type_field.value = item_type;
    item_type_field.name = "item_type";
    form.appendChild(id_field);
    form.appendChild(item_type_field);
    document.body.appendChild(form)
    form.submit();
}

//Converts the time zone from GMT to the time zone on the user's local machine.
function convertTimeZone(userID, year, month, day, hour, minute, second) {
    var GMTString = year + "/" + month + "/" + day + " " +            //Assemble time-related info into a string that JavaScript's Date
                    hour + ":" + minute + ":" + second + " GMT";      //variable accepts.
    var newDate = new Date(GMTString);                                //Initialize date in GMT. This allows JavaScript's Date feature
                                                                      //to keep the GMT time in mind as it automatically converts to client's time zone.
    var timeRow = document.getElementById("time" + userID);           //User ID ensures that all time-entries have a unique JavaScript ID.

    //Example of the time string produced by the following code: Mon, Nov 05, 2018 at 7:45:00 PM
    var dateInfo = newDate.toDateString().split(" ");
    var dateString = dateInfo[0] + ", " + dateInfo[1] + " " +         //Grabs day of the week, month name, day of the month and
                     dateInfo[2] + ", " + dateInfo[3];                //year respectively.

    //Retrieving the time in 12-hour notation is done manually since Safari cannot convert 24-hour to 12-hour
    //with any functions associated with a Date variable.
    var hour = newDate.getHours();
    var amPmString = "AM";
    if (hour >= 12)                                                   //If time is p.m.
    {
        hour = hour % 12
        amPmString = "PM";
    }
    if (hour == 0)                                                    //12:00 is used in am/pm, not 0:00
        hour = 12;
    var timeInfo = newDate.toTimeString().split(":");
    dateString += " at " + hour + ":" + timeInfo[1] + ":" +           //Grab hour in terms of am/pm, minutes, seconds (here, we grab the
                  (timeInfo[2].split(" "))[0] + " " + amPmString;     //seconds value from the unneeded info), alongside the AM/PM prefix.
    timeRow.innerHTML = dateString;
}

function topFunction() {                                              //back to top function; scrolls to the top of the page
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function toggleFilter() {
    document.getElementById("filter").classList.toggle("active");
    document.getElementById("filterRow").classList.toggle("hidden");
}