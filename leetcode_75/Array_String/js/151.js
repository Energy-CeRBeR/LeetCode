/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.split(" ").filter(c => c.length).reverse().join(" ")
};

s = "a good   example"
console.log(reverseWords(s))