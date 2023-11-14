#!/usr/bin/node

/**
 * This script defines a function that executes x times
 * another function
 */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
