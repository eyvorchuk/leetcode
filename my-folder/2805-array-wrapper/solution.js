/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    let sum = 0;
    for (const val of this.nums) {
        sum += val;
    }
    return sum;
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    if (this.nums.length === 0) {
        return "[]"
    }
    let str = "["
    for (let i = 0; i < this.nums.length - 1; i++) {
        str += this.nums[i] + ","
    }
    str += this.nums[this.nums.length - 1] + "]"
    return str;
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
