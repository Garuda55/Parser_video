(function() {
    'use strict';

    let count = 602;
    let nameDate;
    let lectures = [];
    
    try {
        while (count != 395) {
            let preArr = [];
            for (let i = 2; i < (document.getElementById(`yui_3_17_2_2_1719659290031_${count}`).childNodes.length) - 1; i++){
                preArr.push(document.getElementById(`yui_3_17_2_2_1719659290031_${count}`).childNodes[i].innerText);
                nameDate = preArr.filter(el => el.trim() !== '');
            } 
            lectures.push(nameDate);
            count--;
        }
    } catch (TypeError) {
        console.log("stop");
    }
    console.log(lectures);
})();
