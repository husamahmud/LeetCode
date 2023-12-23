/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function (words, x) {
    let idx = [];

    for (let i = 0; i < words.length; i++)
        if (words[i].includes(x)) idx.push(i);

    return idx;
};
