// /**
//  * @param {string} val
//  * @return {Object}
//  */
// var expect = function(val) {
//     return {
//         toBe: (val2) => {
//             if (val !==val2) throw new Error("Not Equal");
//             else return true;
//         },
//         notToBe: (val2) => {
//             if (val === val2) throw new Error("Equal");
//             else return true;
//         }
//     }
// };

function expect(val) {
    return {
        toBe: function(expectedVal) {
            if (val === expectedVal) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: function(expectedVal) {
            if (val !== expectedVal) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
}

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
