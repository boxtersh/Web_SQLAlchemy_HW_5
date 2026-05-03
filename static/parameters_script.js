const port = "1313"

// Запрос получения списка фильмов

let list_btn = document.getElementById('list_btn');
function validation_is_number(field, number, dict_params, default_){
    if (number !== ''){
        number_int = Number(number);
        if (!isNaN(number_int)){
            if (number_int>=default_ && Number.isInteger(number_int)) return dict_params[field] = number_int;
            else alert(`Поле ${field} должно быть целым числом больше либо равным ${default_}!`);
        }
        else alert(`Поле ${field} должно быть числом`);
    }
    else return
}
console.log('list_btn', list_btn);

list_btn.addEventListener('click', () => {
    params = {};
    let skip = document.getElementById('skip').value;
    let limit = document.getElementById('limit').value;
    let yesNoSelect = document.getElementById('yesNoSelect').value;
    validation_is_number('skip', skip, params, 0);
    validation_is_number('limit', limit, params, 1);
    validation_is_number('is_watched', yesNoSelect, params, 0);

    let url = `http://127.0.0.1:${port}/movies`;
    if (Object.keys(params).length !== 0) {url = `http://127.0.0.1:${port}/movies?` + new URLSearchParams(params)};

    window.location.href = url;
});
/*    fetch(url, {
    method: 'GET',
    })
        .then(response => {
            if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(html => {
            document.getElementById('movies-container').innerHTML = html;
            console.log('Успешно! Получен ответ от сервера');
            alert('Список фильмов выгружен!');
        })
        .catch(error => {
            console.error('Ошибка при отправке данных:', error);
            alert('Произошла ошибка при скачивании списка фильмов. Попробуйте ещё раз.');
        });
});
*/