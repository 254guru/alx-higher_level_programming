#!/usr/bin/node

exports.executeXTimes = function (x, theFunction) {
  if (x <= 0) {
    return;
  }
  theFunction();
  exports.executeXTimes(x - 1, theFunction);
};
