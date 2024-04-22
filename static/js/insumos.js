const searchInput = document.getElementById('search-input')
const searchButton = document.getElementById('search-button')
const searchForm = document.getElementById('search-form-insumo')

async function getTalleristas() {
  await new Promise(resolve => setTimeout(resolve, 1000))

  return [
    { id: 1, name: 'Insumo 1' },
    { id: 2, name: 'Insumo 2' },
    { id: 3, name: 'Insumo 3' },
    { id: 4, name: 'Insumo 4' },
    { id: 5, name: 'Insumo 5' },
    { id: 6, name: 'Insumo 6' },
    { id: 7, name: 'Insumo 7' },
    { id: 8, name: 'Insumo 8' },
    { id: 9, name: 'Insumo 9' },
    { id: 10, name: 'Insumo 10' },
  ]
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

  console.log(searchButton.children[0])
  searchButton.children[0].classList.add('rotating')
  searchButton.style.opacity = 0.75

  searchButton.setAttribute('disabled', '')

  searchButton.style.cursor = 'default'
  
  await getTalleristas().then(insumos => {
    console.log(insumos)
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

  console.log(searchInput.value)
})

searchInput.addEventListener('input', e => {
  console.log(e.target.value)
  if (searchInput.value.trim() === '') {
    searchButton.setAttribute('disabled', '')
  } else {
    searchButton.removeAttribute('disabled')
  }
})
