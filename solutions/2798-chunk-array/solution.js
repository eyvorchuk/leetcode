/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const chunkedArr = []
    const nchunks = Math.floor(arr.length / size);
    for (let n = 0; n < nchunks; n++) {
        chunkedArr.push([])
        for (let i = 0; i < size; i++) {
            chunkedArr[n].push(arr[n*size+i])
        }
    }
    if (arr.length % size !== 0) {
        chunkedArr.push([])
        for (let i = nchunks*size; i < arr.length; i++) {
            chunkedArr[nchunks].push(arr[i])
        }
    }
    return chunkedArr;
};

