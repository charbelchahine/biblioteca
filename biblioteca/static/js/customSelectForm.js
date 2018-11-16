function customSelect() {
    if (document.getElementById('id_sort_by') !=null){
        var sortBy = document.getElementById('id_sort_by');
        var sortWrapper = document.createElement('div');
        sortWrapper.innerHTML = sortBy.outerHTML;
        sortWrapper.setAttribute('class', 'custom-select');
        sortWrapper.setAttribute('style', 'width:150px;'); 
        sortBy.parentNode.insertBefore(sortWrapper, sortBy);
        sortBy.remove();
    }
    
    if (document.getElementById('id_type_filter') !=null){
        var typeFilter = document.getElementById('id_type_filter');
        var typeWrapper = document.createElement('div');
        typeWrapper.innerHTML = typeFilter.outerHTML;
        typeWrapper.setAttribute('class', 'custom-select');
        typeWrapper.setAttribute('style', 'width:100px;');
        typeFilter.parentNode.insertBefore(typeWrapper, typeFilter);
        typeFilter.remove();
    }

    if (document.getElementById('id_label_filter') !=null){
        var labelFilter = document.getElementById('id_label_filter');
        var labelWrapper = document.createElement('div');
        labelWrapper.innerHTML = labelFilter.outerHTML;
        labelWrapper.setAttribute('class', 'custom-select');
        labelWrapper.setAttribute('style', 'width:250px;');
        labelFilter.parentNode.insertBefore(labelWrapper, labelFilter);
        labelFilter.remove();
    }

    if (document.getElementById('id_artist_filter') !=null){
        var artistFilter = document.getElementById('id_artist_filter');
        var artistWrapper = document.createElement('div');
        artistWrapper.innerHTML = artistFilter.outerHTML;
        artistWrapper.setAttribute('class', 'custom-select');
        artistWrapper.setAttribute('style', 'width:200px;');
        artistFilter.parentNode.insertBefore(artistWrapper, artistFilter);
        artistFilter.remove();
    }
    if (document.getElementById('id_director_filter') !=null) {
        var directorFilter = document.getElementById('id_director_filter');
        var directorWrapper = document.createElement('div');
        directorWrapper.innerHTML = directorFilter.outerHTML;
        directorWrapper.setAttribute('class', 'custom-select');
        directorWrapper.setAttribute('style', 'width:200px;');
        directorFilter.parentNode.insertBefore(directorWrapper, directorFilter);
        directorFilter.remove();
    }

    if (document.getElementById('id_language_filter') !=null) {
        var languageFilter = document.getElementById('id_language_filter');
        var languageWrapper = document.createElement('div');
        languageWrapper.innerHTML = languageFilter.outerHTML;
        languageWrapper.setAttribute('class', 'custom-select');
        languageWrapper.setAttribute('style', 'width:200px;');
        languageFilter.parentNode.insertBefore(languageWrapper, languageFilter);
        languageFilter.remove();
    }

    if (document.getElementById('id_publisher_filter') !=null) {
        var publisherFilter = document.getElementById('id_publisher_filter');
        var publisherWrapper = document.createElement('div');
        publisherWrapper.innerHTML = publisherFilter.outerHTML;
        publisherWrapper.setAttribute('class', 'custom-select');
        publisherWrapper.setAttribute('style', 'width:250px;');
        publisherFilter.parentNode.insertBefore(publisherWrapper, publisherFilter);
        publisherFilter.remove();
    }

    if (document.getElementById('id_format_filter') !=null) {
        var formatFilter = document.getElementById('id_format_filter');
        var formatWrapper = document.createElement('div');
        formatWrapper.innerHTML = formatFilter.outerHTML;
        formatWrapper.setAttribute('class', 'custom-select');
        formatWrapper.setAttribute('style', 'width:200px;');
        formatFilter.parentNode.insertBefore(formatWrapper, formatFilter);
        formatFilter.remove();
    }

    var x, i, j, selElmnt, a, b, c;
    /*look for any elements with the class "custom-select":*/
    x = document.getElementsByClassName("custom-select");
    for (i = 0; i < x.length; i++) {
      selElmnt = x[i].getElementsByTagName("select")[0];
      /*for each element, create a new DIV that will act as the selected item:*/
      a = document.createElement("DIV");
      a.setAttribute("class", "select-selected");
      a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
      x[i].appendChild(a);
      /*for each element, create a new DIV that will contain the option list:*/
      b = document.createElement("DIV");
      b.setAttribute("class", "select-items select-hide");
      for (j = 0; j < selElmnt.length; j++) {
        /*for each option in the original select element,
        create a new DIV that will act as an option item:*/
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        c.addEventListener("click", function(e) {
            /*when an item is clicked, update the original select box,
            and the selected item:*/
            var y, i, k, s, h;
            s = this.parentNode.parentNode.getElementsByTagName("select")[0];
            h = this.parentNode.previousSibling;
            for (i = 0; i < s.length; i++) {
              if (s.options[i].innerHTML == this.innerHTML) {
                s.selectedIndex = i;
                h.innerHTML = this.innerHTML;
                y = this.parentNode.getElementsByClassName("same-as-selected");
                for (k = 0; k < y.length; k++) {
                  y[k].removeAttribute("class");
                }
                this.setAttribute("class", "same-as-selected");
                break;
              }
            }
            h.click();
        });
        b.appendChild(c);
      }
      x[i].appendChild(b);
      a.addEventListener("click", function(e) {
          /*when the select box is clicked, close any other select boxes,
          and open/close the current select box:*/
          e.stopPropagation();
          closeAllSelect(this);
          this.nextSibling.classList.toggle("select-hide");
          this.classList.toggle("select-arrow-active");
        });
    }
}
function closeAllSelect(elmnt) {
    /*a function that will close all select boxes in the document,
    except the current select box:*/
    var x, y, i, arrNo = [];
    x = document.getElementsByClassName("select-items");
    y = document.getElementsByClassName("select-selected");
    for (i = 0; i < y.length; i++) {
        if (elmnt == y[i]) {
        arrNo.push(i)
        } else {
        y[i].classList.remove("select-arrow-active");
        }
    }
    for (i = 0; i < x.length; i++) {
        if (arrNo.indexOf(i)) {
        x[i].classList.add("select-hide");
        }
    }
}

/*if the user clicks anywhere outside the select box then close all select boxes:*/
document.addEventListener("click", closeAllSelect);