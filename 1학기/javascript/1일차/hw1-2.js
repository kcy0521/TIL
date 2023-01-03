// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log(i)
}
// const 는 상수선언이다. 그래서 i값이 바뀔수 없으므로 오류가 나온다.
// 그래서 i값이 바뀔수 있는 선언인 let 이나 var로 선언해야한다.
// string 값으로 받으라 했으니 String()으로 형변환 시켜준다.

// for (var i = 0; i < nums.length; i++) {}
//                                     ^

// TypeError: Assignment to constant variable.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}
// for ... in 은 속성 이름을 통해 반복되고
// for ... of 는 속성 값을 통해 반복된다.
// 값을 기준으로 해야 number가 나오므로 in을 of 로 바꾸어준다.

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string