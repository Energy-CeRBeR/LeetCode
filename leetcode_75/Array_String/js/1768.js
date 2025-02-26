/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
    let result = []
    let startLength = Math.max(word1.length, word2.length)
    let i = 0
    while (i < startLength) {
        result.push(word1[i])
        result.push(word2[i])
        i++
    }

    if (i < word1.length) {
        result.push(word1[i++])
    }
    if (i < word2.length) {
        result.push(word2[i++])
    }

    return result.join("")
};