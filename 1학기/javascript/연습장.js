// console.log('hello, java');
// console.log('javascripts')
// 이건 주석
/* 
여러줄 주석은
이것으로 표현
*/
// for, if, function 등 예약어 사용 불가능? 식별자
// 카멜케이스 camelCase, lower-camel-case
// let dog // 선언
// dog = 11
// console.log(dog);
// let man = 12 // let 블록스코프 지역변수 동시에 값을 초기화
// console.log(man);
// const userInfo = { name: 'Tom', age:20} //일기전용 상수
// console.log(userInfo);
// let x = 1
// if (x === 1) {
//     let x = 2
//     console.log(x); 
// }
// console.log(x);
// let 으로는 똑같은 이름의 변수 선언못한다.
// 재할당만 가능하다
// const num = 10
// 블록 스코프는 뭔말이누 암튼 이 const는 
// 재선언 재할당 불가능 상수다 항상고정
// var num2 = 10
// console.log(num2);
// num2 = 20
// console.log(num2);
// var num2 = 15
// console.log(num2);
// var 쓰면 문제 발생 가능 따라서 const와let 을 사용 권장
// const nums = [1,2,3,4,5,6,7,8]
// console.log(nums.length);

// 호이스팅이라고 변수들의 위치가 맨위로 끌어 올려지는 현상
// 에어비엔비 에서는 const 권장 재할당필요시만 let 사용
// 실습시에서는 편의를 위해 let 사용을 해도 된다.
// 원시 타입 & 참조 타입
// const a = '1'
// const b = 1
// const name = '김창영'

// const d = `안녕 하세요 ${a}${name} !!`
// const result = Math.PI > 4 ? 'yes' : 'Nope'
// console.log(result);

// null (일부러 값 안씀) undefine(값을 안씀 할당을 못찾음)
// boolean 타입 - 참, 거짓
// 암묵적 타입변환을 한다.
// if (name === '김창'){
//     console.log(`${name} 안녕`)
// } else{
//     console.log('안녕')
// }

// switch (name) {
//     case '김창영':{
//         console.log('환영')
//     }
//     break
//     case'manager':{
//         console.log('hello')
//     }
//     break 

//     default: {
//         console.log(`${name}`);
//     }
    
// }

// 함수를 변수명으로 지정 가능하다 변수로 지정된 함수는 불러오기 불가능함
// ...(인자) 쓰면 끼워넣기 가능하다
// let page = ['1','2']
// let page2 = ['3', ...page, '4']
// console.log(page2);

// 함수 선언식으로 정의한 함수는 var 로 정의한 변수처럼 호이스팅이 발생
// 즉 함수 호출 이후에 선언해도 동작(호이스팅 때문임) -- 파이썬이랑 달라서 신기 기억해놓자
// 선언식과 표현식 정리 호이스팅 없는걸 선호(표현식)

// 배열 메서드 기초 
/*
reverse 원본 배열의 요소들의 순서를 반대로 정렬
push & pop 배열의 맨뒤 요소 추가 제거
unshift & shift 배열의 가장 앞에 추가 제거
includes 배열에 특정값 찾기 참/거짓 반환
indexOf 배열특정값의 인덱스 반환 없으면 -1 반환
join 배열의 모든 요소를 구분자를 이용하여 연결?? 이건 어떻게 표현될까?
*/

// const nums = [1,2,3,4,5]
// nums.push(100)
// nums.reverse()
// nums.pop()
// console.log(nums.join('-'));
// 반복 함수를 사용하여 5번만 별찍기 해야된다.
// 132


