/* 
  아래에 코드를 작성해주세요.
*/

const inputTag = document.querySelector('.search-box__input')

const searchBtn = document.querySelector('.search-box__button')
const resultcard = document.querySelector('.search-result')

function fetchAlbums () {
  const keyword = inputTag.value
  
  const url = 'http://ws.audioscrobbler.com/2.0/?method=album.search&album='+keyword+'&api_key=20afb123cab3bcee1ad0994f0567c343&format=json'
  let page = 1
  let limit = 10

  axios.get(url)
  .then((response) => {
    console.log(response.data.results.albummatches.album);
    const albums = response.data.results.albummatches.album
    
    // const cardname = document.createElement('title')
    for (let i = 0; i < albums.length; i++) {
      
      //이미지 태그 만들기 + 나머지도 만들어봐라
      const cardimg = document.createElement('img')
      cardimg.src = albums[i].image[1]['#text']
      
      const cardname = document.createElement('h2')
      cardname.innerText = albums[i].artist
      
      const albumname = document.createElement('p')
      albumname.innerText = albums[i].name
      
      // div 태크 만들고 클래스 부여하기
      const card = document.createElement('div')
      card.classList.add('search-result__card')
      
      const textcard = document.createElement('div')
      textcard.classList.add('search-result__text')
      
      // div태그에 이미지 태그 추가하기
      
      resultcard.appendChild(card)
      
      card.appendChild(cardimg)
      
      card.appendChild(textcard)
      textcard.appendChild(cardname)
      textcard.appendChild(albumname)
      
      console.log(card);
    }
  })
  . catch((error) => {
    alert('잠시 후 다시 시도해주세요')
  })
}
searchBtn.addEventListener('click', fetchAlbums)

