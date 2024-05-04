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
  e.preventDefault()
  fetch('http://localhost:8000/verificar-tallerista', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    return response.json()
  })
  .then(data => {
    console.log(data)
  })

  verificado = data.verificado ? false : true
  const button = document.getElementById(`verificar-${i}`)

  button.innerHTML = verificado ? "Verificado" : "No verificado"
  button.classList.remove(`tallerista-card__button--${data.verificado}`)
  button.classList.add(`tallerista-card__button--${verificado}`)
}
