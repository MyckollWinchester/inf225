const searchInput = document.getElementById('search-input')
const searchButton = document.getElementById('search-button')
const searchForm = document.getElementById('search-form-talleristas')

async function getTalleristas(prompt) {
  const response = await fetch(`http://localhost:8000/buscar-tallerista/?prompt=${prompt}`)
  return await response.json()
}

async function getExistencia(prompt) {
  const response = await fetch(`http://localhost:8000/buscar-persona-en-db/?prompt=${prompt}`)
  return await response.json()
}

async function getExistencias() {
  const favButtons = document.querySelectorAll('.fav-button');
  favButtons.forEach(async favButton => {
    const card = favButton.parentElement.parentElement;
    const cardLeft = card.children[0];
    const cardProfile = cardLeft.children[1];
    const cardLinkedIn = cardProfile.children[1];
    const linkedin = cardLinkedIn.href;

    const existencia = await getExistencia(linkedin);
    //console.log(linkedin, existencia)
    if (existencia) {
      favButton.children[0].setAttribute('fill', '#1B2027');
      favButton.classList.toggle('fav-button--active');

    }
  });
}

searchForm.addEventListener('submit', async e => {
  e.preventDefault()
  if (searchInput.value.trim() === '') return

  searchButton.innerHTML = `
    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none">
      <path d="M12 3V6M12 18V21M6 12H3M21 12H18M5.63672 5.63672L7.75977 7.75977M16.2422 16.2422L18.3633 18.3633M18.3652 5.63477L16.2441 7.75586M7.75781 16.2422L5.63477 18.3652" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    Buscar
  `

  searchButton.children[0].classList.add('rotating')
  searchButton.style.opacity = 0.75

  searchButton.setAttribute('disabled', '')

  searchButton.style.cursor = 'default'

  await getTalleristas(searchInput.value).then(talleristas => {
    const talleristasSearchResults = document.getElementById('talleristas-search-results')
    talleristasSearchResults.innerHTML = ''

    talleristas.forEach(tallerista => {
      const card = document.createElement('div')
      card.classList.add('card')

      const cardLeft = document.createElement('div')
      cardLeft.classList.add('card__left')

      const cardImage = document.createElement('img')
      cardImage.src = tallerista.foto_perfil
      cardImage.alt = `Foto de perfil de ${tallerista.titulo}`
      cardImage.classList.add('card__image')

      const cardProfile = document.createElement('div')
      cardProfile.classList.add('card__profile')

      const cardName = document.createElement('h1')
      cardName.classList.add('card__name')
      cardName.textContent = tallerista.titulo

      const cardLinkedIn = document.createElement('a')
      cardLinkedIn.href = tallerista.enlace
      cardLinkedIn.classList.add('card__linkedin')
      cardLinkedIn.textContent = 'LinkedIn'
      cardLinkedIn.target = '_blank'
      cardLinkedIn.rel = 'noopener noreferrer'

      cardProfile.appendChild(cardName)
      cardProfile.appendChild(cardLinkedIn)

      cardLeft.appendChild(cardImage)
      cardLeft.appendChild(cardProfile)

      const cardRight = document.createElement('div')
      cardRight.classList.add('card__right')

      const favButton = document.createElement('button')
      favButton.classList.add('fav-button')

      const favButtonSVG = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
      favButtonSVG.setAttribute('width', '32px')
      favButtonSVG.setAttribute('height', '24px')
      favButtonSVG.setAttribute('viewBox', '0 0 24 24')
      favButtonSVG.setAttribute('fill', 'none')

      const favButtonPath = document.createElementNS('http://www.w3.org/2000/svg', 'path')
      favButtonPath.setAttribute('d', 'M11.245 4.174C11.4765 3.50808 11.5922 3.17513 11.7634 3.08285C11.9115 3.00298 12.0898 3.00298 12.238 3.08285C12.4091 3.17513 12.5248 3.50808 12.7563 4.174L14.2866 8.57639C14.3525 8.76592 14.3854 8.86068 14.4448 8.93125C14.4972 8.99359 14.5641 9.04218 14.6396 9.07278C14.725 9.10743 14.8253 9.10947 15.0259 9.11356L19.6857 9.20852C20.3906 9.22288 20.743 9.23007 20.8837 9.36432C21.0054 9.48051 21.0605 9.65014 21.0303 9.81569C20.9955 10.007 20.7146 10.2199 20.1528 10.6459L16.4387 13.4616C16.2788 13.5829 16.1989 13.6435 16.1501 13.7217C16.107 13.7909 16.0815 13.8695 16.0757 13.9507C16.0692 14.0427 16.0982 14.1387 16.1563 14.3308L17.506 18.7919C17.7101 19.4667 17.8122 19.8041 17.728 19.9793C17.6551 20.131 17.5108 20.2358 17.344 20.2583C17.1513 20.2842 16.862 20.0829 16.2833 19.6802L12.4576 17.0181C12.2929 16.9035 12.2106 16.8462 12.1211 16.8239C12.042 16.8043 11.9593 16.8043 11.8803 16.8239C11.7908 16.8462 11.7084 16.9035 11.5437 17.0181L7.71805 19.6802C7.13937 20.0829 6.85003 20.2842 6.65733 20.2583C6.49056 20.2358 6.34626 20.131 6.27337 19.9793C6.18915 19.8041 6.29123 19.4667 6.49538 18.7919L7.84503 14.3308C7.90313 14.1387 7.93218 14.0427 7.92564 13.9507C7.91986 13.8695 7.89432 13.7909 7.85123 13.7217C7.80246 13.6435 7.72251 13.5829 7.56262 13.4616L3.84858 10.6459C3.28678 10.2199 3.00588 10.007 2.97101 9.81569C2.94082 9.65014 2.99594 9.48051 3.11767 9.36432C3.25831 9.23007 3.61074 9.22289 4.31559 9.20852L8.9754 9.11356C9.176 9.10947 9.27631 9.10743 9.36177 9.07278C9.43726 9.04218 9.50414 8.99359 9.55657 8.93125C9.61593 8.86068 9.64887 8.76592 9.71475 8.57639L11.245 4.174Z')
      favButtonPath.setAttribute('stroke', '#1B2027')
      favButtonPath.setAttribute('stroke-width', '2')
      favButtonPath.setAttribute('stroke-linecap', 'round')
      favButtonPath.setAttribute('stroke-linejoin', 'round')

      favButtonSVG.appendChild(favButtonPath)
      favButton.appendChild(favButtonSVG)

      cardRight.appendChild(favButton)

      card.appendChild(cardLeft)
      card.appendChild(cardRight)

      talleristasSearchResults.appendChild(card)
    })

    getExistencias();
  })

  searchButton.style.opacity = 1
  searchButton.children[0].classList.remove('rotating')
  searchButton.innerHTML = `
    <svg width="1rem" height="1rem" fill="currentColor" viewBox="0 0 256 256">
      <path d="M232.49,215.51,185,168a92.12,92.12,0,1,0-17,17l47.53,47.54a12,12,0,0,0,17-17ZM44,112a68,68,0,1,1,68,68A68.07,68.07,0,0,1,44,112Z"></path>
    </svg>
    Buscar
  `

  searchButton.style.cursor = 'pointer'

  searchButton.removeAttribute('disabled')

  const favButtons = document.querySelectorAll('.fav-button')

  favButtons.forEach(favButton => {
    favButton.addEventListener('click', async () => {
      const favButtonSVG = favButton.children[0]
      favButtonSVG.setAttribute('fill', favButton.classList.contains('fav-button--active') ? 'none' : '#1B2027')

      const card = favButton.parentElement.parentElement
      const cardLeft = card.children[0]
      const cardProfile = cardLeft.children[1]
      const cardLinkedIn = cardProfile.children[1]
      const linkedin = cardLinkedIn.href

      if (favButton.classList.contains('fav-button--active')) {
        const cardName = cardProfile.children[0]
        const cardImage = cardLeft.children[0]
        const name = cardName.textContent
        const image = cardImage.src
        const favTallerista = { titulo: name, enlace: linkedin, foto_perfil: image, verificado: false }
        console.log("BORRANDO...")
        console.log(favTallerista)
        await fetch('http://localhost:8000/desmarcar-tallerista/', {
          method: 'POST',
          cors: 'no-cors',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(favTallerista)
        })
          .then(response => {
            return response.json()
          })
          .then(data => {
            if (data.status === 200) {
              console.log('Tallerista eliminado')
              favButton.classList.remove('fav-button--active')
            }
          })
      } else {
        const cardName = cardProfile.children[0]
        const cardImage = cardLeft.children[0]
        const name = cardName.textContent
        const image = cardImage.src
        const favTallerista = { titulo: name, enlace: linkedin, foto_perfil: image, verificado: false }
        console.log("AGREGANDO...")
        console.log(favTallerista)
        await fetch('http://localhost:8000/marcar-tallerista/', {
          method: 'POST',
          cors: 'no-cors',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(favTallerista)
        })
          .then(response => {
            return response.json()
          })
          .then(data => {
            if (data.status === 200) console.log('Tallerista marcado como favorito')
            favButton.classList.toggle('fav-button--active')
          })
      }
    })
  })
})

searchInput.addEventListener('input', () => {
  if (searchInput.value.trim() === '') {
    searchButton.setAttribute('disabled', '')
  } else {
    searchButton.removeAttribute('disabled')
  }
})