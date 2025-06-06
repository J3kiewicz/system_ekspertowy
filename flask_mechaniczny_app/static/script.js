// script.js

// Obiekt do przechowywania odpowiedzi
let answers = {};

// Funkcja do ustawiania wartości i pokazywania następnego pytania
function setValueAndShow(field, value, nextDiv) {
    // Ustawienie wartości w obiekcie odpowiedzi
    answers[field] = value;

    // Ukrycie wszystkich divów
    const allDivs = document.querySelectorAll('div[id]');
    allDivs.forEach(div => {
        div.style.display = 'none';
    });

    // Pokazanie następnego pytania
    document.getElementById(nextDiv).style.display = 'block';

    // Sprawdzenie, czy to ostatnie pytanie
    if (nextDiv === 'submitSection') {
        document.getElementById('submitSection').style.display = 'block';
    }
}

// Funkcja do wysyłania formularza
function submitForm() {
    // Ustawienie wartości w ukrytych polach formularza
    for (const key in answers) {
        const input = document.querySelector(`input[name="${key}"]`);
        if (input) {
            input.value = answers[key];
        }
    }

    // Wysłanie formularza
    document.getElementById('preferenceForm').submit();
}
