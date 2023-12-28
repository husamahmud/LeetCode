/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
    for (let letter of s)
        t = t.replace(letter, "");
    return t;
};

let s = "abcd", t = "abcde";
for (let char of s)
    console.log(t = t.replace(char, ""));
