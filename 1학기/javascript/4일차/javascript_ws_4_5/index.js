// 코드를 작성해 주세요

//결과에 따라 점수 변화

// 왼쪽 = 플레이어 v
// 오른쪽 = 컴퓨터, 무작위 선택 v
// 클릭시 플레이어의 선택이 결정 v
// 클릭시 비활성화 v
// 3초간 컴퓨터의 결과가 0.1초 단위로 가위바위보순서대로 변경 v
// modal이 천천히 나타난다.클릭시 사라짐 결과가 포함되어있음
// modal사라지면 게임 반복가능

const section = document.querySelector('section')

const mm = document.querySelector('.modal')
const modalTag = document.querySelector('.modal-content')

const sbtn = document.querySelector('#scissors-button')
const rbtn = document.querySelector('#rock-button')
const pbtn = document.querySelector('#paper-button')

const p1img = document.querySelector('#player1-img')
const p1number = document.querySelector('.countA')
let p1 = 0

const p2img = document.querySelector('#player2-img')
const p2number = document.querySelector('.countB')
let p2 = 0




rbtn.addEventListener('click', function (event) {
    const cases = [sbtn, rbtn, pbtn]
    let cnt = 0
    // 버튼을 클릭했을때 이미지src 바뀜
    p1img.setAttribute('src', './img/rock.png')
    
    // p2의 이미지 바뀌고 그 정해진다.
    const pick = setInterval(function () {
        p2img.setAttribute('src', cases[cnt % 3].firstElementChild.getAttribute('src'))
        cnt++
    }, 100)
    setTimeout(function () {
        clearInterval(pick)
        p2img.setAttribute('src', cases[parseInt(Math.random() * 10 )% 3].firstElementChild.getAttribute('src'))
        
        mm.style.display = 'flex'

        if (p2img.getAttribute('src') === sbtn.firstElementChild.getAttribute('src')) {
            p1 += 1
            p1number.innerText = p1
            modalTag.innerText = 'player1이 이겼습니다.'
        } 
        if (p2img.getAttribute('src') === rbtn.firstElementChild.getAttribute('src')) {
            modalTag.innerText = '비겼습니다.'
        } 
        if (p2img.getAttribute('src') === pbtn.firstElementChild.getAttribute('src')) {
            p2 +=1
            p2number.innerText = p2
            modalTag.innerText = 'player2이 이겼습니다.'
        }
    }, 3000)
 })

 pbtn.addEventListener('click', function (event) {
    const cases = [sbtn, rbtn, pbtn]
    let cnt = 0
    // 버튼을 클릭했을때 이미지src 바뀜
    p1img.setAttribute('src', './img/paper.png')
    
    // p2의 이미지 바뀌고 그 정해진다.
    const pick = setInterval(function () {
        p2img.setAttribute('src', cases[cnt % 3].firstElementChild.getAttribute('src'))
        cnt++
    }, 100)
    setTimeout(function () {
        clearInterval(pick)
        p2img.setAttribute('src', cases[parseInt(Math.random() * 10 )% 3].firstElementChild.getAttribute('src'))
        
        mm.style.display = 'flex'

        if (p2img.getAttribute('src') === sbtn.firstElementChild.getAttribute('src')) {
            p2 += 1
            p2number.innerText = p2
            modalTag.innerText = 'player2이 이겼습니다.'
        } 
        if (p2img.getAttribute('src') === rbtn.firstElementChild.getAttribute('src')) {
            p1 +=1
            p1number.innerText = p1
            modalTag.innerText = 'player1이 이겼습니다.'
        } 
        if (p2img.getAttribute('src') === pbtn.firstElementChild.getAttribute('src')) {
            modalTag.innerText = '비겼습니다.'
        }
    }, 3000)
 })

 sbtn.addEventListener('click', function (event) {
    const cases = [sbtn, rbtn, pbtn]
    let cnt = 0
    // 버튼을 클릭했을때 이미지src 바뀜
    p1img.setAttribute('src', './img/scissors.png')
    
    // p2의 이미지 바뀌고 그 정해진다.
    const pick = setInterval(function () {
        p2img.setAttribute('src', cases[cnt % 3].firstElementChild.getAttribute('src'))
        cnt++
    }, 100)
    setTimeout(function () {
        clearInterval(pick)
        p2img.setAttribute('src', cases[parseInt(Math.random() * 10 )% 3].firstElementChild.getAttribute('src'))
        
        mm.style.display = 'flex'

        if (p2img.getAttribute('src') === sbtn.firstElementChild.getAttribute('src')) {
            modalTag.innerText = '비겼습니다.'
        } 
        if (p2img.getAttribute('src') === rbtn.firstElementChild.getAttribute('src')) {
            p2 +=1
            p2number.innerText = p2
            modalTag.innerText = 'player2이 이겼습니다.'
        } 
        if (p2img.getAttribute('src') === pbtn.firstElementChild.getAttribute('src')) {
            p1 +=1
            p1number.innerText = p1
            modalTag.innerText = 'player1이 이겼습니다.'
        }
    }, 3000)
 })

 mm.addEventListener('click', function (event) {
    mm.style.display = 'none'
 })