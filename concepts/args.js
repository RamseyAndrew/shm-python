function args(array) {
  for (let value of array) {
    console.log(value);
  }
}

args([]);

function add(array) {
  let ans = 0;
  for (let value of array) {
    ans = ans + value;
  }

  return ans;
}

add([10, 20, 30]); 

