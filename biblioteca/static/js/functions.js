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
    var GMTString = year + " " + month + " " + day + " " +        //Assemble time-related info into a string that JavaScript's Date
                    hour + ":" + minute + ":" + second + " GMT";  //variable accepts.
    var newDate = new Date(GMTString);                            //Initialize date in GMT. This allows JavaScript's Date feature
                                                                  //to keep the GMT time in mind as it automatically converts to client's time zone.
    var timeRow = document.getElementById("time" + userID);       //User ID ensures that all time-entries have a unique JavaScript ID.
    timeRow.innerHTML = newDate.toDateString() + " " + newDate.toLocaleTimeString();
}