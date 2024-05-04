const searchInput = document.getElementById('search-input')
const searchButton = document.getElementById('search-button')
const searchForm = document.getElementById('search-form-insumo')

async function getInsumos(prompt) {
  const response = await fetch(`http://localhost:8000/buscar-insumo/?prompt=${prompt}`)
  const data = await response.json()
  return data
  // const response = await fetch('static/json/dummy-insumos.json')
  // return data = response.json()
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
  
  await getInsumos(searchInput.value).then(insumos => {
    const insumosRes = document.getElementById('insumo-search-results')
    insumosRes.innerHTML = ''

    insumos.forEach(insumo => {
      const card = document.createElement('div')
      card.classList.add('insumo-card')

      const imageContainer = document.createElement('div')
      imageContainer.classList.add('insumo-card__image-container')

      const image = document.createElement('img')
      image.src = insumo.imagen
      image.classList.add('insumo-card__image')

      const name = document.createElement('h1')
      name.classList.add('insumo-card__name')
      name.innerHTML = insumo.nombre

      const price = document.createElement('h2')
      price.classList.add('insumo-card__price')
      const formattedPrice = insumo.precio.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.')
      price.innerHTML = `$${formattedPrice}`

      const button = document.createElement('a')
      button.classList.add('button', 'insumo-card__button')
      button.href = insumo.enlace
      button.target = '_blank'
      button.rel = 'noopener noreferrer'
      button.innerHTML = 'Abrir en Jumbo'

      imageContainer.appendChild(image)
      card.appendChild(imageContainer)
      card.appendChild(name)
      card.appendChild(price)
      card.appendChild(button)

      insumosRes.appendChild(card)
    })
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
})

searchInput.addEventListener('input', e => {
  console.log(e.target.value)
  if (searchInput.value.trim() === '') {
    searchButton.setAttribute('disabled', '')
  } else {
    searchButton.removeAttribute('disabled')
  }
})
