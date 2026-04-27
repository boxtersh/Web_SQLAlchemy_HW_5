let btn = document.getElementById('btn');
let title = document.getElementById('title');
let genre = document.getElementById('genre');
let release_year = document.getElementById('release_year');

btn.addEventListener('click', () => {
    title_text = title.value
    genre_text = genre.value
    release_year_text = release_year.value
    if (!title_text || !genre_text || !release_year_text) {
        alert('Пожалуйста, заполните все поля, они не должны быть пусты!');
        return;
    }

    const movieData = {
        title: title_text,
        genre: genre_text,
        release_year: release_year_text
    };
    console.log('movieData=', movieData)

    fetch('http://????????????????????????????????/api/movies', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(movieData)
    })
        .then(response => {
            if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Успешно! Получен ответ от сервера:', data);
            alert('Фильм успешно добавлен!');
        })
        .catch(error => {
            console.error('Ошибка при отправке данных:', error);
            alert('Произошла ошибка при сохранении фильма. Попробуйте ещё раз.');
        });
});






/* СТАРОЕ
const btnTask1 = document.getElementsByClassName('btn-dark')[0];
const pTask1 = document.getElementById('pTask1');

btnTask1.addEventListener('click', () => {
    pTask1.classList.toggle('text-color-blue');
});


const btnTask2 = document.getElementsByClassName('btn-info')[0];
const inputTask2 = document.getElementById('inputTask2');
btnTask2.addEventListener('click', () => {
    inputTask2.value = '';
});


const btnTask3 = document.getElementsByClassName('btn-success')[0];
const inputTask3 = document.getElementById('inputTask3');
const pTask3 = document.querySelector('.task3>p');
btnTask3.addEventListener('click', () => {
    pTask3.textContent = inputTask3.value;
    inputTask3.value = '';
});


const btnTask4 = document.querySelector('.task4>button');
const divTask4 = document.querySelector('.task4>div');
btnTask4.addEventListener('click', () => {
    if (divTask4.classList.contains('color-blue'))
    divTask4.classList.remove('color-blue');
    else divTask4.classList.add('color-blue');
});


const btnTask5 = document.querySelector('.task5>button');
const divTask5 = document.querySelector('.task5');
let ulTask5 = document.createElement('ul');
btnTask5.addEventListener('click', () => {
    for(let i=0; i<10; i++) {
    let liTask5 = document.createElement('li');
    liTask5.textContent = `Пункт ${i}`;
    if (i%2==0) liTask5.classList.add('liTask5-color');
    ulTask5.append(liTask5);
    }
    divTask5.append(ulTask5);
});


const btnTask6 = document.querySelector('.task6>button');
const h6Task6 = document.querySelector('.task6>h6');
btnTask6.addEventListener('click', () => {
    h6Task6.classList.toggle('hide');
});


const btn1Task7 = document.querySelector('.task7 .btn-dark');
const btn2Task7 = document.querySelector('.task7 .btn-info');
const h6Task7 = document.querySelector('.task7>h6');
btn1Task7.addEventListener('click', () => {
    if (h6Task7.classList.contains('font-size33')){
    h6Task7.classList.remove('font-size33')}
});
btn2Task7.addEventListener('click', () => {
    if (!h6Task7.classList.contains('font-size33')){
    h6Task7.classList.add('font-size33')}
});


const imgTask8 = document.querySelector('.task8 img');
imgTask8.addEventListener('mouseenter', () => {
    imgTask8.setAttribute("src", "/image/1.png");
});

imgTask8.addEventListener('mouseleave', () => {
    imgTask8.setAttribute("src", "/image/2.png");
});


const btnTask9 = document.querySelector('.task9 .btn-dark');
const divTask9 = document.querySelector('.task9 div');
btnTask9.addEventListener('click', () => {
    divTask9.classList.toggle('modified');
});

const selectTask11 = document.querySelector('.form-select');
const btnTask11 = document.querySelector('.task11 .btn-dark');
let pTask11 = document.getElementById('p-text-color');
btnTask11.addEventListener('click', () => {
    let textcolor = selectTask11.options[selectTask11.selectedIndex].text;
    color=textcolor=='Выберете цвет для абзаца ниже'? 'black': textcolor;
    pTask11.style.color = color;
});


let input1Task12 = document.getElementById('input1Task12');
let input2Task12 = document.getElementById('input2Task12');
let btnTask12 = document.querySelector('.task12 button');
const errorNumber = 'Это не число';
const errorEmpty = 'Поля не должны быть пустыми';
btnTask12.addEventListener('click', () => {
    value1 = input1Task12.value;
    value2 = input2Task12.value;
    if (input1Task12.value === '' || input2Task12.value === '') alert(errorEmpty);
    else {
        if (typeof value1 === 'number') alert(`${value1} errorNumber`);
        else {
            if (typeof value2 === 'number') alert(`${value2} errorNumber`);
            else {
                let res = value1>value2 ? 1:2;
                alert(`Число больше в ${res} поле`)
                input1Task12.value = '';
                input2Task12.value = '';
            }
        }
    }
});


let btnTask13 = document.querySelector('.task13 button');
let pTask13 = document.querySelector('#counting');
let count = 0;
btnTask13.addEventListener('click', () => {
    count++;
    pTask13.textContent = count;
    if (count==10) btnTask13.disabled = true;
});


let btnTask14 = document.querySelector('.task14 button');
let ulTask14 = document.createElement('ul');
btnTask14.addEventListener('click', () => {
    for (let i=1; i<6; i++) {
    let liTask14 = document.createElement('li');
    liTask14.textContent=`Пункт №${i}`
    ulTask14.append(liTask14);
    }
    btnTask14.after(ulTask14);
});
*/