const N = parseInt(
  require("fs")
    .readFileSync("./input.txt")
    .toString()
);
for (let i = 1; i <= N; i++) {
  console.log("*".repeat(i));
}
for (let i = N - 1; i >= 1; i--) {
  console.log("*".repeat(i));
}
