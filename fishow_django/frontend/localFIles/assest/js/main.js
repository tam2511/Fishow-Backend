const waitElement = (element, callback) => {
    const tick = () => {
        timerId = setTimeout(tick, 200);
        if (document.querySelector(element)) {
            clearTimeout(timerId);
            callback(document.querySelectorAll(element));
        }
    };
    let timerId = setTimeout(tick, 100);
};
const getCoords = elem => {
    let box = elem.getBoundingClientRect();

    return {
        top: box.top + pageYOffset,
        left: box.left + pageXOffset
    };
};

document.body.addEventListener("click", event => {
    if (event.target.classList.contains("rd-nav-link")) {
        localStorage.setItem("active_tab", event.target.innerText);
    }
    if (event.target.classList.contains("fishow-blog_image__close-button")) {
        event.target.parentNode.parentNode.remove();
    }
});
const activeTab = localStorage.getItem("active_tab");
waitElement(".rd-nav-link", elements => {
    [].slice.call(elements).forEach(button => {
        if (button.innerText === activeTab) {
            button.parentNode.classList.toggle("active");
        }
    });
});

const waitLoadingImage = (image) => {
    waitElement(`#fishow-picture${image}`, (thisElement) => {
        addEventHandler(thisElement[0], 'change', function() {
            readURL(this);
        });
    });

};

let counter = 1;
const addElementOnPage = (type,selector) => {
    let counterText = 0;
    let counterImage = 0;

    waitElement(selector, button => {
        button[0].addEventListener("click", () => {

            const closeButton = document.createElement('div');
            const formWrap = document.createElement("div");
            formWrap.classList.add('form-wrap');
            closeButton.classList.add('fishow-blog_image__close-button');
            closeButton.innerText = 'x';
            formWrap.insertAdjacentElement("afterbegin", closeButton);
            if (type === 'textarea') {
                counterText++;
                const label = document.createElement('label');
                const textarea = document.createElement('textarea');
                const span = document.createElement('span');

                textarea.classList.add('form-input');
                textarea.classList.add('form-control-has-validation');
                textarea.classList.add('form-control-last-child');
                textarea.id = `form-text_${counterText}`;
                textarea.setAttribute('name', `text_${counterText}`);


                label.classList.add('form-label');
                label.classList.add('rd-input-label');
                label.setAttribute('for',`form-text_${counterText}`);
                label.innerText = 'Текст';

                span.classList.add('form-validation');

                formWrap.insertAdjacentElement("beforeend", label);
                formWrap.insertAdjacentElement("beforeend", textarea);
                formWrap.insertAdjacentElement("beforeend", span);
            } else {
                waitLoadingImage(counter);
                document.getElementById(`fishow-picture${counter}`).click();
                const image = document.createElement('img');
                counter++;
                counterImage++;
                image.src = '#';
                image.width = '500';
                image.height = '500';
                // image.alt = `pic_${counterImage}`;
                image.setAttribute('data-image', counterImage);
                image.id = `form-image_${counter}`;
                image.setAttribute('name', `image_${counter}`);
                const inputImage = `<input
                                    class="form-input"
                                    id="fishow-picture${counter}"
                                    type="file"
                                    name="picture"
                            />`;
                document.querySelector('.fishow_button_picture .fishow_action_btn').insertAdjacentHTML("beforebegin", inputImage);
                formWrap.classList.add('fishow-blog_image');
                formWrap.insertAdjacentElement("beforeend", image);
            }
            const containter = document.createElement('div');
            containter.classList.add('col-md-12');
            containter.classList.add('fishow-content');
            containter.insertAdjacentElement("afterbegin", formWrap);
            const fishowContent = document.querySelectorAll(".fishow-content");
            const length = fishowContent.length - 1;
            fishowContent[length].insertAdjacentElement("afterend", containter);
        });
    });
};

addElementOnPage('textarea',".fishow_button_text .fishow_action_btn");
addElementOnPage('picture',".fishow_button_picture .fishow_action_btn");

const addEventHandler = (elem, eventType, handler) => {
    if (elem.addEventListener)
        elem.addEventListener (eventType, handler, false);
    else if (elem.attachEvent)
        elem.attachEvent ('on' + eventType, handler);
};
const readURL = (input) => {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            const lastImage = document.querySelectorAll('.fishow-blog_image img');
            const lastImagelength = document.querySelectorAll('.fishow-blog_image img').length - 1;
            lastImage[lastImagelength].setAttribute('src', e.target.result); // img
        };
        reader.readAsDataURL(input.files[0]);
    }
};



const delSpaces = (str) => str.replace(/\s/g, '');

document.querySelectorAll('[data-vote-status]').forEach((ele) => console.log(ele.getAttribute('data-vote-status')));
const handler = (element, selector) => {
    const vote = selector === '.fishow-votes_up' ? 'like' : 'dislike';
    console.log('like dislike? = ', vote);
    const id = parseInt(element.parentNode.querySelector('[data-votes-counter]').id);
    let voteStatus = element.parentNode.querySelector('[data-vote-status]').getAttribute('data-vote-status');
    voteStatus = delSpaces(voteStatus);
    console.log('voteStatus = ', voteStatus);
    fetch("http://127.0.0.1:8000/", {
        "credentials": "include",
        "headers": {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        },
        "referrer": "http://127.0.0.1:8000/",
        "body": `id_item=${id}&type_buttons=${vote}`,
        "method": "POST",
        "mode": "cors"
    }).then((response) => {
        if (response.status === 500) {
            console.error('ошбика запроса');
        } else if (response.status === 200) {
            console.table(response);
            console.log('fine');
        }
        return response;
    })
};



const doVote = (selectorsButtons) => {
    waitElement(selectorsButtons, (elements) => {
        const buttonsVoteUp = [].slice.call(elements);
        buttonsVoteUp.forEach((button) => {
            button.addEventListener('click', (event) => handler(event.currentTarget.parentNode, selectorsButtons));
        });
    });
};
doVote('.fishow-votes_down');
doVote('.fishow-votes_up');
// function wish_func(form,id,type_button)
// {
//     $.ajax(
//         {
//             type:"POST",
//             url: "",
//             data:{
//
//                 id_item: $('#'+id).val(),
//                 type_buttons : type_button
//
//             },
//             success: function( data )
//             {
//
//                 if (type_button=='like')
//                 {
//                     if( $('#'+id+'_rating_trig').val()=='0')
//                     {
//                         $('#'+id+'_rating').html( parseInt($('#'+id+'_rating').text()) + 1);
//                         $('#'+id+'_rating_trig').html($('#'+id+'_rating_trig').val(1));
//                     } else if( $('#'+id+'_rating_trig').val() =='-1')
//                     {
//                         $('#'+id+'_rating').html( parseInt($('#'+id+'_rating').text()) + 1);
//                         $('#'+id+'_rating_trig').html($('#'+id+'_rating_trig').val(1));
//                     }
//
//                 }
//                 if (type_button=='dislike')
//                 {
//                     if( $('#'+id+'_rating_trig').val()=='0')
//                     {
//                         $('#'+id+'_rating').html( parseInt($('#'+id+'_rating').text()) - 1);
//                         $('#'+id+'_rating_trig').html($('#'+id+'_rating_trig').val(-1));
//                     } else if( $('#'+id+'_rating_trig').val() =='1')
//                     {
//                         $('#'+id+'_rating').html( parseInt($('#'+id+'_rating').text()) - 1);
//                         $('#'+id+'_rating_trig').html($('#'+id+'_rating_trig').val(-1));
//                     }
//                 }
//                 return true
//             }
//         });
//
//     return false;
//
// }