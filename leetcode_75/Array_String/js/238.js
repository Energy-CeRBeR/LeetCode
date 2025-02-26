/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    let n = nums.length
    let pref1 = [1]
    let pref2 = [1]
    for (let i = 0; i < n; ++i) {
        pref1.push(pref1[i] * nums[i])
        pref2.push(pref2[i] * nums[n - i - 1])
    }
    pref2.reverse()

    let result = []
    for (let i = 0; i < n; ++i) {
        result.push(pref1[i] * pref2[i + 1])
    }

    return result
};