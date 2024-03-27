#!/usr/bin/node

const request = require('request');

try {
  const URL = process.argv[2];

  request(URL, (error, response, body) => {
    if (error) throw error;
    const tasks = JSON.parse(body);
    const completed = {};
    for (const task of tasks) {
      if (task.completed) {
        if (completed[task.userId]) {
          completed[task.userId] += 1;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  });
} catch (error) {
  console.error(error);
}
