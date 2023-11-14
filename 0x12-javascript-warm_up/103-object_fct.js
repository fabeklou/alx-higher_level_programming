#!/usr/bin/node

/**
 * This script implements an increment function in an object
 */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* adding an anonymous function to an object */
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
