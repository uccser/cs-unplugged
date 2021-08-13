/**
* Takes an encoded HTML entitity and returns a decoded version of it.
* @param {string} str 
* @returns decoded HTML entity
*/
function decodeHTMLEntities (str) {
    let element = document.createElement('div');
    if(str && typeof str === 'string') {
    // strip script/html tags
    str = str.replace(/<script[^>]*>([\S\s]*?)<\/script>/gmi, '');
    str = str.replace(/<\/?\w(?:[^"'>]|"[^"]*"|'[^']*')*>/gmi, '');
    element.innerHTML = str;
    str = element.textContent;
    element.textContent = '';
    }

    return str;
}

exports.decodeHTMLEntities = decodeHTMLEntities;
