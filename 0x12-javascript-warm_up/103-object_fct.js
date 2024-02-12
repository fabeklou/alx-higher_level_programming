#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/**
 * Regular functions have their own this context.
 * And this is determined dynamically depending on how you call
 * or execute the function. Arrow functions, on the other hand,
 * do not have their own this context.
 */
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
