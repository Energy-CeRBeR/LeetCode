/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
    if (str2.length > str1.length) {
        return gcdOfStrings(str2, str1)
    }

    if (!str1.startsWith(str2)) {
        return ""
    }

    if (str2.length == 0) {
        return str1
    }

    return gcdOfStrings(str1.slice(str2.length, str1.length), str2)
};