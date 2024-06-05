const talleristasPh = document.getElementById('talleristas-ph')

const talleristas = fetch('http://localhost:8000/talleristas')

talleristas.then(response => {
  return response.json()
}).then(data => {
  if (data.length > 0) {
    talleristasPh.innerHTML = ''
    talleristasPh.classList.remove('note')
    talleristasPh.style.display = 'flex'
    talleristasPh.style.flexDirection = 'column'
    talleristasPh.style.gap = '16px'

    let i = 0

    data.forEach(tallerista => {
      i++
      const card = document.createElement('div')
      card.classList.add('tallerista-card')

      const image = document.createElement('img')
      image.src = tallerista.foto_perfil
      image.classList.add('tallerista-card__image')

      const div = document.createElement('div')

      const title = document.createElement('h1')
      title.classList.add('tallerista-card__title')
      title.innerHTML = tallerista.titulo

      const ul = document.createElement('ul')

      const li = document.createElement('li')
      li.classList.add('tallerista-card__contact')

      li.innerHTML = `&#10095;<a href="${tallerista.enlace}" class="tallerista-card__linkedin">${tallerista.enlace}</a>
      <a id="verificar-${i}" href="" class="button button--green tallerista-card__button tallerista-card__button--${tallerista.verificado}">${tallerista.verificado ? "Verificado" : "No verificado" }</a>`

      ul.appendChild(li)
      div.appendChild(title)
      div.appendChild(ul)
      card.appendChild(image)
      card.appendChild(div)
      console.log(card)
      talleristasPh.appendChild(card)
    })

    for (let i = 1; i <= data.length; i++) {
      const button = document.getElementById(`verificar-${i}`)
      button.addEventListener('click', e => {
        verificarTallerista(e, i, data[i - 1])
      })
    }
  }
})

const verificarTallerista = (e, i, data) => {
  e.preventDefault();
  fetch('http://localhost:8000/verificar-tallerista', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    return response.json();
  })
  .then(updatedData => {
    console.log(updatedData);
    data.verificado = updatedData.verificado;

    const button = document.getElementById(`verificar-${i}`);

    button.innerHTML = data.verificado ? "Verificado" : "No verificado";
    button.classList.remove(`tallerista-card__button--${!data.verificado}`);
    button.classList.add(`tallerista-card__button--${data.verificado}`);
  });
};


const insumosPh = document.getElementById('insumos-ph')

const insumos = fetch('http://localhost:8000/insumos')

insumos.then(response => {
  return response.json()
}).then(data => {
  if (data.length > 0) {
    insumosPh.innerHTML = ''
    insumosPh.classList.remove('note')
    insumosPh.style.display = 'flex'
    insumosPh.style.flexDirection = 'column'
    insumosPh.style.gap = '16px'

    let i = 0

    data.forEach(insumo => {
      i++
      const card = document.createElement('div')
      card.classList.add('insumo-card')
      card.id = `insumo-card-${i}`

      const imageContainer = document.createElement('div')
      imageContainer.classList.add('insumo-card__image-container')

      const image = document.createElement('img')
      image.src = insumo.foto
      image.classList.add('insumo-card__image')

      const name = document.createElement('h1')
      name.classList.add('insumo-card__name')
      name.innerHTML = insumo.nombre

      const price = document.createElement('h2')
      price.classList.add('insumo-card__price')
      price.innerHTML = insumo.precio

      const button = document.createElement('a')
      button.classList.add('button', 'insumo-card__button')
      button.href = insumo.enlace
      button.target = '_blank'
      button.rel = 'noopener noreferrer'
      button.innerHTML = 'Abrir en Jumbo'

      imageContainer.appendChild(image)

      const deleteButton = document.createElement('button')
      deleteButton.classList.add('fav-button')
      
      const deleteButtonSVG = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
      deleteButtonSVG.setAttribute('width', '32px')
      deleteButtonSVG.setAttribute('height', '24px')
      deleteButtonSVG.setAttribute('viewBox', '0 0 24 24')
      deleteButtonSVG.setAttribute('fill', 'none')
      
      const deleteButtonPath = document.createElementNS('http://www.w3.org/2000/svg', 'path')
      deleteButtonPath.setAttribute('d', 'M18 6L6 18M6 6l12 12')
      deleteButtonPath.setAttribute('stroke', '#1B2027')
      deleteButtonPath.setAttribute('stroke-width', '2')
      deleteButtonPath.setAttribute('stroke-linecap', 'round')
      deleteButtonPath.setAttribute('stroke-linejoin', 'round')
      
      deleteButtonSVG.appendChild(deleteButtonPath)
      deleteButton.id = `eliminar-insumo-${i}`
      deleteButton.appendChild(deleteButtonSVG)
      

      card.appendChild(imageContainer)
      card.appendChild(name)
      card.appendChild(price)
      card.appendChild(button)
      card.appendChild(deleteButton)

      insumosPh.appendChild(card)
    })
    
    for (let i = 1; i <= data.length; i++) {
      const button = document.getElementById(`eliminar-insumo-${i}`)
      button.addEventListener('click', e => {
        eliminarInsumo(e, i, data[i - 1])
      })
    }
  }
})

const eliminarInsumo = (e, i, data) => {
  e.preventDefault();
  fetch('http://localhost:8000/desmarcar-insumo/', {
    method: 'POST',
    cors: 'no-cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    return response.json()
  })
  .then(data => {
    if (data.status === 200) {
      console.log('Inusmo eliminado')
      document.getElementById(`insumo-card-${i}`).remove();
    }
  })
};