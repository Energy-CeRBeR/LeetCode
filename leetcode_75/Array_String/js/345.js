/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
    const vowels = "aeiouAEIOU"
    let left = 0
    let right = s.length - 1
    let listS = s.split("")
    while (left <= right) {
        if (vowels.includes(s[left])) {
            while (left <= right && !vowels.includes(s[right])) {
                right--
            }
            if (left <= right) {
                let t = listS[left]
                listS[left] = listS[right]
                listS[right] = t
                right--
            }
        }
        left++

    }

    return listS.join("")
};