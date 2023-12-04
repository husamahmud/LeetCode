/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
    const anagram = new Map()

    for (let str of strs) {
        let sorted = str.split('').sort().join('')

        if (anagram.has(sorted))
            anagram.get(sorted).push(str)
        else
            anagram.set(sorted, [str])
    }

    return Array.from(anagram.values())
};
