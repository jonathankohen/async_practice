const fetch = require('node-fetch');
const fs = require('fs');

const loadFile = async () => {
    try {
        const data = await fs.promises.readFile('./text.txt', {
            encoding: 'utf-8',
        });
        console.log(data);
    } catch (err) {
        console.log(err);
    }
};

loadFile();

const fetchP = async id => {
    try {
        const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
        const data = await res.json();
        console.log(data);
    } catch (err) {
        console.error(err);
    }
};

fetchP(2);
