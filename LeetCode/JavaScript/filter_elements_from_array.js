/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var a = []
    for(let i=0;i<arr.length;i++){
        var ans = fn(arr[i],i);
        if (ans){
            a.push(arr[i]);
        }
    }
    return a;
};
